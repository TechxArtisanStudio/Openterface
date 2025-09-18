#!/usr/bin/env python3
"""
Link Extraction Module
Scans markdown and HTML files to extract all URLs and links
"""

import re
import csv
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

from config import (
    SCAN_DIRECTORIES, EXCLUDE_DIRECTORIES, OUTPUT_DIR, 
    LINK_PATTERNS, CSV_COLUMNS, SUPPORTED_LANGUAGES
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/extract_links.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class LinkExtractor:
    def __init__(self):
        self.extracted_links = []
        self.file_stats = {'processed': 0, 'errors': 0}
        
    def should_exclude_file(self, file_path: Path) -> bool:
        """Check if file should be excluded from processing"""
        path_str = str(file_path)
        return any(exclude_dir in path_str for exclude_dir in EXCLUDE_DIRECTORIES)
    
    def detect_language_from_filename(self, file_path: Path) -> str:
        """Detect language from filename pattern (e.g., filename.zh.md)"""
        filename = file_path.name
        
        # Check for language suffix pattern: .lang.md or .lang.html
        for lang in SUPPORTED_LANGUAGES.keys():
            if f'.{lang}.' in filename:
                return lang
                
        # Default to English if no language suffix found
        return 'en'
    
    def extract_markdown_links(self, content: str, file_path: Path, language: str) -> List[Dict]:
        """Extract links from markdown content"""
        links = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Markdown images: ![alt](url)
            for match in re.finditer(LINK_PATTERNS['markdown_image'], line):
                alt_text = match.group(1)
                url = match.group(2)
                
                links.append({
                    'file_path': str(file_path),
                    'line_number': line_num,
                    'link_type': 'markdown_image',
                    'link_text': alt_text,
                    'raw_url': url,
                    'is_external': url.startswith(('http://', 'https://')),
                    'is_image': True,
                    'language': language,
                    'context': line.strip()
                })
            
            # Markdown links: [text](url)
            for match in re.finditer(LINK_PATTERNS['markdown_link'], line):
                link_text = match.group(1)
                url = match.group(2)
                
                links.append({
                    'file_path': str(file_path),
                    'line_number': line_num,
                    'link_type': 'markdown_link',
                    'link_text': link_text,
                    'raw_url': url,
                    'is_external': url.startswith(('http://', 'https://')),
                    'is_image': False,
                    'language': language,
                    'context': line.strip()
                })
        
        return links
    
    def extract_html_links(self, content: str, file_path: Path, language: str) -> List[Dict]:
        """Extract links from HTML content"""
        links = []
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Parse HTML with BeautifulSoup (using built-in parser)
            soup = BeautifulSoup(line, 'html.parser')
            
            # Extract img src attributes
            for img in soup.find_all('img'):
                src = img.get('src')
                alt = img.get('alt', '')
                if src:
                    links.append({
                        'file_path': str(file_path),
                        'line_number': line_num,
                        'link_type': 'html_img',
                        'link_text': alt,
                        'raw_url': src,
                        'is_external': src.startswith(('http://', 'https://')),
                        'is_image': True,
                        'language': language,
                        'context': line.strip()
                    })
            
            # Extract href attributes
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                text = link.get_text(strip=True) or ''
                if href:
                    links.append({
                        'file_path': str(file_path),
                        'line_number': line_num,
                        'link_type': 'html_link',
                        'link_text': text,
                        'raw_url': href,
                        'is_external': href.startswith(('http://', 'https://')),
                        'is_image': False,
                        'language': language,
                        'context': line.strip()
                    })
            
            # Also check for href and src attributes in raw HTML (for cases where BeautifulSoup might miss them)
            # HTML img src
            for match in re.finditer(LINK_PATTERNS['html_img_src'], line, re.IGNORECASE):
                src = match.group(1)
                links.append({
                    'file_path': str(file_path),
                    'line_number': line_num,
                    'link_type': 'html_img_raw',
                    'link_text': '',
                    'raw_url': src,
                    'is_external': src.startswith(('http://', 'https://')),
                    'is_image': True,
                    'language': language,
                    'context': line.strip()
                })
            
            # HTML href
            for match in re.finditer(LINK_PATTERNS['html_href'], line, re.IGNORECASE):
                href = match.group(1)
                links.append({
                    'file_path': str(file_path),
                    'line_number': line_num,
                    'link_type': 'html_link_raw',
                    'link_text': '',
                    'raw_url': href,
                    'is_external': href.startswith(('http://', 'https://')),
                    'is_image': False,
                    'language': language,
                    'context': line.strip()
                })
        
        return links
    
    def process_file(self, file_path: Path) -> List[Dict]:
        """Process a single file and extract all links"""
        try:
            language = self.detect_language_from_filename(file_path)
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            links = []
            
            if file_path.suffix == '.md':
                links.extend(self.extract_markdown_links(content, file_path, language))
            elif file_path.suffix == '.html':
                links.extend(self.extract_html_links(content, file_path, language))
            
            self.file_stats['processed'] += 1
            return links
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            self.file_stats['errors'] += 1
            return []
    
    def scan_directory(self, directory: Path) -> List[Dict]:
        """Scan a directory for files and extract links"""
        all_links = []
        
        if not directory.exists():
            logger.warning(f"Directory does not exist: {directory}")
            return all_links
        
        # Find all markdown and HTML files
        files = []
        for pattern in ['**/*.md', '**/*.html']:
            files.extend(directory.glob(pattern))
        
        logger.info(f"Found {len(files)} files to process in {directory}")
        
        for file_path in tqdm(files, desc=f"Processing {directory.name}"):
            if self.should_exclude_file(file_path):
                continue
                
            links = self.process_file(file_path)
            all_links.extend(links)
        
        return all_links
    
    def save_results(self, links: List[Dict]):
        """Save extracted links to CSV files organized by language"""
        if not links:
            logger.warning("No links found to save")
            return
        
        # Group links by language
        links_by_language = {}
        for link in links:
            lang = link['language']
            if lang not in links_by_language:
                links_by_language[lang] = []
            links_by_language[lang].append(link)
        
        # Save CSV for each language
        for language, lang_links in links_by_language.items():
            output_file = OUTPUT_DIR / language / 'links_extracted.csv'
            
            df = pd.DataFrame(lang_links)
            df.to_csv(output_file, index=False, encoding='utf-8')
            
            logger.info(f"Saved {len(lang_links)} links for {language} to {output_file}")
        
        # Save combined results
        combined_file = OUTPUT_DIR / 'all_languages_links_extracted.csv'
        df_all = pd.DataFrame(links)
        df_all.to_csv(combined_file, index=False, encoding='utf-8')
        
        logger.info(f"Saved {len(links)} total links to {combined_file}")
        
        # Print summary statistics
        self.print_summary(links_by_language)
    
    def print_summary(self, links_by_language: Dict[str, List[Dict]]):
        """Print summary statistics"""
        print("\n" + "="*60)
        print("LINK EXTRACTION SUMMARY")
        print("="*60)
        print(f"Files processed: {self.file_stats['processed']}")
        print(f"Files with errors: {self.file_stats['errors']}")
        print(f"Total links extracted: {sum(len(links) for links in links_by_language.values())}")
        print("\nBy Language:")
        
        for language, links in links_by_language.items():
            external_count = sum(1 for link in links if link['is_external'])
            image_count = sum(1 for link in links if link['is_image'])
            print(f"  {language}: {len(links)} links ({external_count} external, {image_count} images)")
        
        print("\nBy Link Type:")
        all_links = [link for links in links_by_language.values() for link in links]
        link_types = {}
        for link in all_links:
            link_type = link['link_type']
            link_types[link_type] = link_types.get(link_type, 0) + 1
        
        for link_type, count in sorted(link_types.items()):
            print(f"  {link_type}: {count}")

def main():
    """Main function to run link extraction"""
    print("Starting link extraction...")
    
    extractor = LinkExtractor()
    all_links = []
    
    # Process each scan directory
    for directory in SCAN_DIRECTORIES:
        logger.info(f"Scanning directory: {directory}")
        links = extractor.scan_directory(directory)
        all_links.extend(links)
    
    # Save results
    extractor.save_results(all_links)
    
    print(f"\nLink extraction completed! Check the 'data' directory for results.")

if __name__ == "__main__":
    main()
