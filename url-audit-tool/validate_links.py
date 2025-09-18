#!/usr/bin/env python3
"""
Link Validation Module
Validates URLs by checking their accessibility with rate limiting and error handling
"""

import time
import logging
from pathlib import Path
from typing import List, Dict, Optional, Set
from urllib.parse import urlparse
import requests
import pandas as pd
from tqdm import tqdm
from collections import defaultdict

from config import (
    OUTPUT_DIR, VALIDATION_CONFIG, SUPPORTED_LANGUAGES, CSV_COLUMNS
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/validate_links.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LinkValidator:
    def __init__(self):
        self.validation_results = []
        self.validation_stats = {
            'total_validated': 0,
            'valid_links': 0,
            'invalid_links': 0,
            'timeout_errors': 0,
            'connection_errors': 0,
            'http_errors': 0,
            'other_errors': 0
        }
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': VALIDATION_CONFIG['user_agent']})
        
        # Cache to avoid validating the same URL multiple times
        self.validation_cache = {}
        
        # Track URLs by domain for rate limiting
        self.domain_last_request = {}
    
    def should_skip_validation(self, url: str) -> bool:
        """Check if URL should be skipped from validation"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Skip localhost and local domains
            if domain in VALIDATION_CONFIG['skip_validation_domains']:
                return True
            
            # Skip MkDocs template variables
            if '{{' in url and '}}' in url:
                return True
                
            return False
        except Exception:
            return True
    
    def wait_for_domain_rate_limit(self, url: str):
        """Implement rate limiting per domain"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            if domain in self.domain_last_request:
                time_since_last = time.time() - self.domain_last_request[domain]
                if time_since_last < VALIDATION_CONFIG['delay_between_requests']:
                    sleep_time = VALIDATION_CONFIG['delay_between_requests'] - time_since_last
                    time.sleep(sleep_time)
            
            self.domain_last_request[domain] = time.time()
        except Exception:
            pass  # Continue if parsing fails
    
    def validate_url(self, url: str) -> Dict:
        """Validate a single URL"""
        # Check cache first
        if url in self.validation_cache:
            return self.validation_cache[url]
        
        result = {
            'url': url,
            'status_code': None,
            'response_time': None,
            'error_message': None,
            'is_valid': False,
            'redirect_url': None,
            'content_type': None,
            'file_size': None
        }
        
        # Skip validation for certain URLs
        if self.should_skip_validation(url):
            result['is_valid'] = True
            result['error_message'] = 'Skipped (local/template variable)'
            self.validation_cache[url] = result
            return result
        
        # Apply rate limiting
        self.wait_for_domain_rate_limit(url)
        
        try:
            start_time = time.time()
            
            # Make request with timeout and follow redirects
            response = self.session.head(
                url, 
                timeout=VALIDATION_CONFIG['timeout'],
                allow_redirects=True
            )
            
            response_time = time.time() - start_time
            
            result.update({
                'status_code': response.status_code,
                'response_time': round(response_time, 3),
                'is_valid': 200 <= response.status_code < 400,
                'redirect_url': response.url if response.url != url else None,
                'content_type': response.headers.get('content-type', ''),
                'file_size': response.headers.get('content-length')
            })
            
            if not result['is_valid']:
                result['error_message'] = f'HTTP {response.status_code}'
                self.validation_stats['http_errors'] += 1
            
        except requests.exceptions.Timeout:
            result['error_message'] = 'Request timeout'
            self.validation_stats['timeout_errors'] += 1
        except requests.exceptions.ConnectionError as e:
            result['error_message'] = f'Connection error: {str(e)}'
            self.validation_stats['connection_errors'] += 1
        except requests.exceptions.RequestException as e:
            result['error_message'] = f'Request error: {str(e)}'
            self.validation_stats['other_errors'] += 1
        except Exception as e:
            result['error_message'] = f'Unexpected error: {str(e)}'
            self.validation_stats['other_errors'] += 1
        
        # Update statistics
        self.validation_stats['total_validated'] += 1
        if result['is_valid']:
            self.validation_stats['valid_links'] += 1
        else:
            self.validation_stats['invalid_links'] += 1
        
        # Cache the result
        self.validation_cache[url] = result
        return result
    
    def load_resolved_links(self, language: str = None) -> List[Dict]:
        """Load resolved links from CSV files"""
        links = []
        
        if language:
            # Load specific language
            csv_file = OUTPUT_DIR / language / 'links_resolved.csv'
            if csv_file.exists():
                df = pd.read_csv(csv_file)
                links = df.to_dict('records')
                logger.info(f"Loaded {len(links)} resolved links for language: {language}")
            else:
                logger.warning(f"No resolved links file found for language: {language}")
        else:
            # Load all languages
            for lang in SUPPORTED_LANGUAGES.keys():
                csv_file = OUTPUT_DIR / lang / 'links_resolved.csv'
                if csv_file.exists():
                    df = pd.read_csv(csv_file)
                    lang_links = df.to_dict('records')
                    links.extend(lang_links)
                    logger.info(f"Loaded {len(lang_links)} resolved links for language: {lang}")
        
        return links
    
    def process_links_for_validation(self, links: List[Dict]) -> List[Dict]:
        """Process links and prepare for validation"""
        # Get unique URLs to validate
        unique_urls = set()
        url_info = defaultdict(list)
        
        for link in links:
            url = link['full_url']
            unique_urls.add(url)
            url_info[url].append({
                'file_path': link['file_path'],
                'line_number': link['line_number'],
                'language': link['language']
            })
        
        logger.info(f"Found {len(unique_urls)} unique URLs to validate")
        
        # Validate each unique URL
        validation_results = []
        for url in tqdm(unique_urls, desc="Validating URLs"):
            validation_result = self.validate_url(url)
            
            # Add usage information
            usage_info = url_info[url]
            validation_result.update({
                'usage_count': len(usage_info),
                'file_locations': '; '.join([f"{info['file_path']}:{info['line_number']}" for info in usage_info]),
                'language': usage_info[0]['language'] if usage_info else 'unknown'
            })
            
            validation_results.append(validation_result)
        
        return validation_results
    
    def save_validation_results(self, results: List[Dict]):
        """Save validation results to CSV files"""
        if not results:
            logger.warning("No validation results to save")
            return
        
        # Group results by language
        results_by_language = defaultdict(list)
        for result in results:
            lang = result.get('language', 'unknown')
            results_by_language[lang].append(result)
        
        # Save CSV for each language
        for language, lang_results in results_by_language.items():
            output_file = OUTPUT_DIR / language / 'links_validated.csv'
            
            df = pd.DataFrame(lang_results)
            df.to_csv(output_file, index=False, encoding='utf-8')
            
            logger.info(f"Saved {len(lang_results)} validation results for {language} to {output_file}")
        
        # Save combined results
        combined_file = OUTPUT_DIR / 'all_languages_links_validated.csv'
        df_all = pd.DataFrame(results)
        df_all.to_csv(combined_file, index=False, encoding='utf-8')
        
        logger.info(f"Saved {len(results)} total validation results to {combined_file}")
        
        # Save broken links report
        broken_links = [r for r in results if not r['is_valid']]
        if broken_links:
            broken_file = OUTPUT_DIR / 'broken_links_report.csv'
            df_broken = pd.DataFrame(broken_links)
            df_broken.to_csv(broken_file, index=False, encoding='utf-8')
            logger.info(f"Saved {len(broken_links)} broken links to {broken_file}")
        
        # Print summary statistics
        self.print_summary(results)
    
    def print_summary(self, results: List[Dict]):
        """Print summary statistics"""
        print("\n" + "="*60)
        print("LINK VALIDATION SUMMARY")
        print("="*60)
        print(f"Total URLs validated: {self.validation_stats['total_validated']}")
        print(f"Valid links: {self.validation_stats['valid_links']}")
        print(f"Invalid links: {self.validation_stats['invalid_links']}")
        print(f"Timeout errors: {self.validation_stats['timeout_errors']}")
        print(f"Connection errors: {self.validation_stats['connection_errors']}")
        print(f"HTTP errors: {self.validation_stats['http_errors']}")
        print(f"Other errors: {self.validation_stats['other_errors']}")
        
        # Success rate
        if self.validation_stats['total_validated'] > 0:
            success_rate = (self.validation_stats['valid_links'] / self.validation_stats['total_validated']) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        # Top error messages
        error_counts = defaultdict(int)
        for result in results:
            if result['error_message']:
                error_counts[result['error_message']] += 1
        
        if error_counts:
            print("\nTop Error Messages:")
            for error, count in sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
                print(f"  {error}: {count}")
        
        # Response time statistics
        response_times = [r['response_time'] for r in results if r['response_time'] is not None]
        if response_times:
            avg_time = sum(response_times) / len(response_times)
            max_time = max(response_times)
            min_time = min(response_times)
            print(f"\nResponse Times:")
            print(f"  Average: {avg_time:.3f}s")
            print(f"  Min: {min_time:.3f}s")
            print(f"  Max: {max_time:.3f}s")

def main():
    """Main function to run link validation"""
    print("Starting link validation...")
    print(f"Note: This may take a while due to rate limiting ({VALIDATION_CONFIG['delay_between_requests']}s between requests)")
    
    validator = LinkValidator()
    
    # Load resolved links
    links = validator.load_resolved_links()
    
    if not links:
        print("No resolved links found. Please run resolve_urls.py first.")
        return
    
    # Process links for validation
    validation_results = validator.process_links_for_validation(links)
    
    # Save results
    validator.save_validation_results(validation_results)
    
    print(f"\nLink validation completed! Check the 'data' directory for results.")

if __name__ == "__main__":
    main()
