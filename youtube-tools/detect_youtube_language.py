#!/usr/bin/env python3
"""
YouTube Language Detection Script

This script uses a local LLM via LM Studio to detect the language of YouTube videos
based on their title and description, then updates the language column in the CSV.

Usage:
    python detect_youtube_language.py [--dry-run] [--verbose] [--force] [--api-url URL]
"""

import os
import re
import sys
import csv
import time
import argparse
import json
from pathlib import Path
from typing import List, Dict, Optional
import requests

# Supported language codes
SUPPORTED_LANGUAGES = ['en', 'zh', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ro']


class LanguageDetector:
    """Detects language using LM Studio API."""
    
    def __init__(self, api_url: str = "http://127.0.0.1:1234/v1/chat/completions", verbose: bool = False):
        self.api_url = api_url
        self.verbose = verbose
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })
        # Disable proxy for localhost connections
        self.session.trust_env = False
        # Explicitly set no_proxy for localhost
        self.session.proxies = {
            'http': None,
            'https': None
        }
        self.model_name = None
        self._get_available_model()
    
    def _get_available_model(self):
        """Get the first available model from LM Studio."""
        try:
            models_url = self.api_url.replace('/v1/chat/completions', '/v1/models')
            response = self.session.get(models_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                if 'data' in data and len(data['data']) > 0:
                    # Prefer chat completion models, fallback to first model
                    for model in data['data']:
                        model_id = model.get('id', '')
                        # Prefer models that look like chat models
                        if 'chat' in model_id.lower() or 'gpt' in model_id.lower() or 'llama' in model_id.lower():
                            self.model_name = model_id
                            break
                    else:
                        # Use first model if no chat model found
                        self.model_name = data['data'][0].get('id', 'local-model')
                    if self.verbose:
                        print(f"Using model: {self.model_name}")
                else:
                    self.model_name = 'local-model'
            else:
                if self.verbose:
                    print(f"Warning: Could not get models list (HTTP {response.status_code}), using 'local-model'")
                self.model_name = 'local-model'
        except Exception as e:
            if self.verbose:
                print(f"Warning: Could not get models list ({e}), using 'local-model'")
            self.model_name = 'local-model'
        
    def detect_language(self, title: str, description: str) -> Optional[str]:
        """Detect language from title and description using LLM."""
        # Prepare the text to analyze
        text_to_analyze = f"Title: {title}\n\nDescription: {description[:500]}"  # Limit description length
        
        prompt = f"""Analyze the following YouTube video title and description, and determine the primary language.

Supported language codes:
- en (English)
- zh (Chinese)
- ja (Japanese)
- ko (Korean)
- fr (French)
- de (German)
- it (Italian)
- es (Spanish)
- pt (Portuguese)
- ro (Romanian)

Text to analyze:
{text_to_analyze}

Respond with ONLY the language code (e.g., "en", "zh", "ja"). Do not include any explanation or additional text."""

        try:
            payload = {
                "model": self.model_name or "local-model",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.1,  # Low temperature for consistent results
                "max_tokens": 50  # Increased to ensure we get a response
            }
            
            if self.verbose:
                print(f"    Calling LLM API...", end='', flush=True)
            
            response = self.session.post(self.api_url, json=payload, timeout=30)
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    
                    # Debug: show full response in verbose mode
                    if self.verbose:
                        print(f"\n    Full API response: {json.dumps(data, indent=2)[:500]}")
                    
                    # Try different response formats
                    content = None
                    if 'choices' in data and len(data['choices']) > 0:
                        choice = data['choices'][0]
                        if 'message' in choice:
                            content = choice['message'].get('content', '').strip()
                        elif 'text' in choice:
                            content = choice['text'].strip()
                        elif 'delta' in choice and 'content' in choice['delta']:
                            content = choice['delta']['content'].strip()
                    
                    # Also try direct 'content' field
                    if not content and 'content' in data:
                        content = data['content'].strip()
                    
                    if not content:
                        if self.verbose:
                            print(f"    Warning: No content found in response. Response keys: {list(data.keys())}")
                        return None
                    
                    # Extract language code from response
                    language_code = self._extract_language_code(content)
                    
                    if self.verbose:
                        print(f"    Raw response: '{content}' -> Language code: {language_code}")
                    
                    return language_code
                except (KeyError, IndexError, json.JSONDecodeError) as e:
                    if self.verbose:
                        print(f"    Error parsing response: {e}")
                        print(f"    Response text: {response.text[:200]}")
                    return None
            else:
                error_msg = f"HTTP {response.status_code}"
                if response.text:
                    error_msg += f": {response.text[:200]}"
                if self.verbose:
                    print(f"    Error: {error_msg}")
                else:
                    print(f"    ✗ API Error: {error_msg}")
                return None
                
        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error: Could not connect to {self.api_url}. Is LM Studio running?"
            print(f"    ✗ {error_msg}")
            if self.verbose:
                print(f"    Details: {e}")
            return None
        except requests.exceptions.Timeout as e:
            error_msg = "Request timeout: API took too long to respond"
            print(f"    ✗ {error_msg}")
            if self.verbose:
                print(f"    Details: {e}")
            return None
        except requests.exceptions.RequestException as e:
            error_msg = f"Request error: {e}"
            print(f"    ✗ {error_msg}")
            return None
        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            print(f"    ✗ {error_msg}")
            if self.verbose:
                import traceback
                traceback.print_exc()
            return None
    
    def _extract_language_code(self, text: str) -> Optional[str]:
        """Extract language code from LLM response."""
        text = text.strip().upper()
        
        # Try to find a language code in the response
        # Look for codes like "en", "zh", etc.
        for lang_code in SUPPORTED_LANGUAGES:
            if lang_code.upper() in text or f'"{lang_code}"' in text or f"'{lang_code}'" in text:
                return lang_code
        
        # Try regex pattern matching
        pattern = r'\b(en|zh|ja|ko|fr|de|it|es|pt|ro)\b'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).lower()
        
        return None
    
    def convert_natural_language_to_code(self, user_input: str) -> Optional[str]:
        """Convert natural language description to language code using LLM."""
        prompt = f"""The user described a language in natural language. Convert it to a language code.

User input: "{user_input}"

Supported language codes:
- en (English)
- zh (Chinese)
- ja (Japanese)
- ko (Korean)
- fr (French)
- de (German)
- it (Italian)
- es (Spanish)
- pt (Portuguese)
- ro (Romanian)

If the user mentioned a language that matches one of the above, respond with ONLY the language code (e.g., "en", "zh", "ja").
If the language is not in the supported list, or if the user said they don't know, respond with "unknown".
Do not include any explanation or additional text."""

        try:
            payload = {
                "model": self.model_name or "local-model",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.1,
                "max_tokens": 20
            }
            
            response = self.session.post(self.api_url, json=payload, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                if 'choices' in data and len(data['choices']) > 0:
                    choice = data['choices'][0]
                    if 'message' in choice:
                        content = choice['message'].get('content', '').strip()
                        if content and content.lower() != 'unknown':
                            return self._extract_language_code(content)
            return None
        except Exception:
            return None


class YouTubeLanguageUpdater:
    """Updates YouTube CSV file with detected languages."""
    
    CSV_COLUMNS = ['youtube_url', 'title', 'author_name', 'thumbnail_url', 'date', 'views', 
                   'description', 'fetch_date', 'z_index', 'language', 'product', 'type', 'home_page']
    
    def __init__(self, csv_path: Path, dry_run: bool = False, verbose: bool = False,
                 force: bool = False, interactive: bool = False,
                 api_url: str = "http://127.0.0.1:1234/v1/chat/completions"):
        self.csv_path = csv_path
        self.dry_run = dry_run
        self.verbose = verbose
        self.force = force
        self.interactive = interactive
        self.detector = LanguageDetector(api_url=api_url, verbose=verbose)
        
    def read_csv(self) -> List[Dict[str, str]]:
        """Read CSV file and return list of rows."""
        rows = []
        
        if not self.csv_path.exists():
            print(f"Error: CSV file not found: {self.csv_path}")
            return rows
            
        try:
            with open(self.csv_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Normalize keys (remove BOM if present)
                    normalized_row = {}
                    for key, value in row.items():
                        normalized_key = key.lstrip('\ufeff')
                        normalized_row[normalized_key] = value
                    
                    # Skip rows where youtube_url is empty or is the header
                    url = normalized_row.get('youtube_url', '').strip()
                    if url and url != 'youtube_url':
                        rows.append(normalized_row)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            
        return rows
    
    def write_csv(self, rows: List[Dict[str, str]]):
        """Write rows to CSV file."""
        if self.dry_run:
            print(f"[DRY RUN] Would write {len(rows)} rows to {self.csv_path}")
            return
            
        try:
            # Create backup
            backup_path = self.csv_path.with_suffix('.csv.backup')
            if self.csv_path.exists():
                import shutil
                shutil.copy2(self.csv_path, backup_path)
                if self.verbose:
                    print(f"Created backup: {backup_path}")
            
            # Determine all columns: start with standard columns, then add any extra columns from rows
            all_columns = list(self.CSV_COLUMNS)
            for row in rows:
                for key in row.keys():
                    if key not in all_columns:
                        all_columns.append(key)
            
            with open(self.csv_path, 'w', encoding='utf-8-sig', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=all_columns)
                writer.writeheader()
                writer.writerows(rows)
                
            print(f"Updated CSV file: {self.csv_path}")
            
        except Exception as e:
            print(f"Error writing CSV file: {e}")
            raise
    
    def needs_detection(self, row: Dict[str, str]) -> bool:
        """Check if a row needs language detection."""
        url = row.get('youtube_url', '').strip()
        if not url:
            return False
        
        title = row.get('title', '').strip()
        description = row.get('description', '').strip()
        
        # Need title or description to detect language
        if not title and not description:
            return False
        
        # If force mode, always detect
        if self.force:
            return True
        
        # Otherwise, only detect if language is empty
        language = row.get('language', '').strip()
        return not language
    
    def detect_and_update(self):
        """Detect language for all rows and update CSV."""
        print("=" * 60)
        print("YouTube Language Detection")
        print("=" * 60)
        
        rows = self.read_csv()
        
        if not rows:
            print("❌ No rows found in CSV file.")
            return
        
        total_rows = len(rows)
        print(f"\n📊 Found {total_rows} rows in CSV file.")
        
        # Count rows that need detection
        rows_to_process = [i for i, row in enumerate(rows) if self.needs_detection(row)]
        rows_to_skip = total_rows - len(rows_to_process)
        
        if rows_to_skip > 0:
            print(f"⏭️  {rows_to_skip} rows will be skipped (already have language)")
        
        if not rows_to_process:
            print("\n✅ All rows already have language codes. No updates needed.")
            return
        
        print(f"🔄 {len(rows_to_process)} rows will be processed.\n")
        
        updated_count = 0
        skipped_count = 0
        success_count = 0
        failed_count = 0
        
        for idx, i in enumerate(rows_to_process, 1):
            row = rows[i]
            url = row.get('youtube_url', '').strip()
            title = row.get('title', '').strip()
            description = row.get('description', '').strip()
            
            if not title and not description:
                skipped_count += 1
                if self.verbose:
                    print(f"  [{idx}/{len(rows_to_process)}] ⚠️  Skipping row {i+1} (no title or description)")
                continue
            
            # Show progress
            progress_pct = int((idx / len(rows_to_process)) * 100) if len(rows_to_process) > 0 else 0
            title_preview = title[:40] + '...' if len(title) > 40 else title
            print(f"  [{idx}/{len(rows_to_process)}] ({progress_pct}%) Detecting language for: {title_preview}")
            
            # Detect language
            language_code = self.detector.detect_language(title, description)
            
            if language_code:
                row['language'] = language_code
                rows[i] = row
                updated_count += 1
                success_count += 1
                print(f"    ✓ Detected: {language_code}")
            else:
                # Interactive mode: ask user for help
                if self.interactive:
                    print(f"\n    🔍 Failed to detect language automatically")
                    print(f"    📺 Video URL: {url}")
                    print(f"    📝 Title: {title}")
                    print(f"\n    Please open the video to check the language.")
                    print(f"    You can respond with:")
                    print(f"      - A language name (e.g., 'Czech', 'English', 'Japanese')")
                    print(f"      - 'skip' or 'unknown' to leave it blank")
                    print(f"      - Press Enter to skip")
                    
                    user_input = input(f"\n    What language is this video? ").strip()
                    
                    if user_input and user_input.lower() not in ['skip', 'unknown', '']:
                        # Use LLM to convert natural language to code
                        print(f"    🤖 Converting '{user_input}' to language code...")
                        detected_code = self.detector.convert_natural_language_to_code(user_input)
                        
                        if detected_code:
                            row['language'] = detected_code
                            rows[i] = row
                            updated_count += 1
                            success_count += 1
                            print(f"    ✓ Set language to: {detected_code}")
                        else:
                            print(f"    ⚠️  Could not convert to language code. Leaving blank.")
                            updated_count += 1
                            failed_count += 1
                    else:
                        print(f"    ⏭️  Skipped. Leaving language blank.")
                        updated_count += 1
                        failed_count += 1
                    print()  # Add blank line after interaction
                else:
                    updated_count += 1
                    failed_count += 1
                    print(f"    ✗ Failed to detect language")
            
            # Add small delay to avoid overwhelming the API
            time.sleep(0.5)
        
        # Final summary
        print("\n" + "=" * 60)
        print("📈 Summary")
        print("=" * 60)
        print(f"  ✅ Successfully detected: {success_count} rows")
        if failed_count > 0:
            print(f"  ❌ Failed to detect: {failed_count} rows")
        print(f"  ⏭️  Skipped: {skipped_count} rows")
        print(f"  📝 Total processed: {updated_count} rows")
        print("=" * 60)
        
        if updated_count > 0:
            self.write_csv(rows)
            print(f"\n💾 CSV file updated: {self.csv_path}")
        else:
            print("\n✅ No updates needed.")


def main():
    parser = argparse.ArgumentParser(
        description='Detect YouTube video languages using local LLM (LM Studio)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Detect language for rows with empty language field
  python detect_youtube_language.py
  
  # Force detect language for all rows (overwrites existing)
  python detect_youtube_language.py --force
  
  # Use custom API URL
  python detect_youtube_language.py --api-url http://localhost:8080/v1/chat/completions
  
  # Dry run to see what would be detected
  python detect_youtube_language.py --dry-run --verbose
  
  # Interactive mode for failed detections
  python detect_youtube_language.py --interactive
        """
    )
    parser.add_argument('--csv-path', 
                       help='Path to CSV file (default: youtube-tools/youtube.csv)',
                       type=Path)
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Enable verbose output')
    parser.add_argument('--force', action='store_true',
                       help='Force detection for all rows, overwriting existing language codes')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Interactive mode: prompt user for failed detections')
    parser.add_argument('--api-url', 
                       default='http://127.0.0.1:1234/v1/chat/completions',
                       help='LM Studio API URL (default: http://127.0.0.1:1234/v1/chat/completions)')
    
    args = parser.parse_args()
    
    # Determine CSV path
    if args.csv_path:
        csv_path = Path(args.csv_path)
    else:
        # Default to youtube-tools/youtube.csv (same directory as script)
        script_dir = Path(__file__).parent
        csv_path = script_dir / "youtube.csv"
    
    print(f"Using LM Studio API: {args.api_url}")
    print(f"CSV file: {csv_path}\n")
    
    # Test API connection first
    if not args.dry_run:
        print("Testing API connection...")
        test_detector = LanguageDetector(api_url=args.api_url, verbose=args.verbose)
        test_result = test_detector.detect_language("Hello World", "This is a test description in English")
        if test_result:
            print(f"✓ API connection successful. Test detection: {test_result}\n")
        else:
            print("⚠️  API connection test failed. Please check:")
            print("  1. Is LM Studio running?")
            print("  2. Is the API server enabled in LM Studio?")
            print("  3. Is a model loaded in LM Studio?")
            print("  4. Try running with --verbose to see detailed errors\n")
            if not args.verbose:
                print("   Run with --verbose for more details.\n")
    
    updater = YouTubeLanguageUpdater(
        csv_path=csv_path,
        dry_run=args.dry_run,
        verbose=args.verbose,
        force=args.force,
        interactive=args.interactive,
        api_url=args.api_url
    )
    
    updater.detect_and_update()


if __name__ == "__main__":
    main()

