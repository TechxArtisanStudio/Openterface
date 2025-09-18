#!/usr/bin/env python3
"""
Master URL Audit Tool
Orchestrates all URL audit modules and provides command-line interface
"""

import argparse
import logging
import sys
from pathlib import Path
from datetime import datetime

# Import all modules
from extract_links import LinkExtractor
from resolve_urls import URLResolver
from validate_links import LinkValidator
from generate_reports import ReportGenerator

from config import OUTPUT_DIR, REPORTS_DIR, LOGS_DIR, SUPPORTED_LANGUAGES, SCAN_DIRECTORIES

# Setup logging
def setup_logging(verbose: bool = False):
    """Setup logging configuration"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOGS_DIR / 'url_audit.log'),
            logging.StreamHandler()
        ]
    )

def run_extraction(language: str = None, verbose: bool = False):
    """Run link extraction"""
    print("🔍 Extracting links from files...")
    extractor = LinkExtractor()
    
    all_links = []
    for directory in SCAN_DIRECTORIES:
        print(f"  Scanning {directory}...")
        links = extractor.scan_directory(directory)
        all_links.extend(links)
    
    extractor.save_results(all_links)
    print(f"✅ Link extraction completed: {len(all_links)} links found")
    return len(all_links)

def run_resolution(language: str = None, verbose: bool = False):
    """Run URL resolution"""
    print("🔗 Resolving URLs...")
    resolver = URLResolver()
    
    links = resolver.load_extracted_links(language)
    if not links:
        print("❌ No extracted links found. Run extraction first.")
        return 0
    
    resolved_links = []
    for link in links:
        resolved_link = resolver.process_link(link)
        resolved_links.append(resolved_link)
    
    resolver.save_resolved_links(resolved_links)
    print(f"✅ URL resolution completed: {len(resolved_links)} URLs resolved")
    return len(resolved_links)

def run_validation(language: str = None, verbose: bool = False):
    """Run link validation"""
    print("🌐 Validating links...")
    validator = LinkValidator()
    
    links = validator.load_resolved_links(language)
    if not links:
        print("❌ No resolved links found. Run resolution first.")
        return 0
    
    validation_results = validator.process_links_for_validation(links)
    validator.save_validation_results(validation_results)
    
    valid_count = sum(1 for r in validation_results if r['is_valid'])
    invalid_count = len(validation_results) - valid_count
    print(f"✅ Link validation completed: {valid_count} valid, {invalid_count} invalid")
    return len(validation_results)

def run_reporting(language: str = None, verbose: bool = False):
    """Run report generation"""
    print("📊 Generating reports...")
    generator = ReportGenerator()
    
    df = generator.load_validation_data(language)
    if df.empty:
        print("❌ No validation data found. Run validation first.")
        return 0
    
    summary_report = generator.generate_summary_report(df)
    broken_links_df = generator.generate_broken_links_report(df)
    frequency_df = generator.generate_url_frequency_analysis(df)
    domain_df = generator.generate_domain_analysis(df)
    
    generator.save_reports(summary_report, broken_links_df, frequency_df, domain_df)
    generator.print_report_summary(summary_report, len(broken_links_df))
    
    print(f"✅ Report generation completed: {len(broken_links_df)} broken links found")
    return len(df)

def run_full_audit(language: str = None, verbose: bool = False):
    """Run complete URL audit pipeline"""
    print("🚀 Starting complete URL audit...")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    try:
        # Step 1: Extract links
        links_found = run_extraction(language, verbose)
        if links_found == 0:
            print("❌ No links found. Exiting.")
            return
        
        # Step 2: Resolve URLs
        urls_resolved = run_resolution(language, verbose)
        if urls_resolved == 0:
            print("❌ URL resolution failed. Exiting.")
            return
        
        # Step 3: Validate links
        urls_validated = run_validation(language, verbose)
        if urls_validated == 0:
            print("❌ Link validation failed. Exiting.")
            return
        
        # Step 4: Generate reports
        reports_generated = run_reporting(language, verbose)
        
        print("\n" + "="*60)
        print("🎉 COMPLETE URL AUDIT FINISHED!")
        print("="*60)
        print(f"Links found: {links_found}")
        print(f"URLs resolved: {urls_resolved}")
        print(f"URLs validated: {urls_validated}")
        print(f"Reports generated: {reports_generated}")
        print(f"\nCheck the following directories for results:")
        print(f"  - Data: {OUTPUT_DIR}")
        print(f"  - Reports: {REPORTS_DIR}")
        print(f"  - Logs: {LOGS_DIR}")
        
    except KeyboardInterrupt:
        print("\n❌ Audit interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Audit failed with error: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

def main():
    """Main command-line interface"""
    parser = argparse.ArgumentParser(
        description="URL Audit Tool for Openterface Documentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python url_audit.py                    # Run complete audit
  python url_audit.py --extract-only     # Extract links only
  python url_audit.py --resolve-only     # Resolve URLs only
  python url_audit.py --validate-only    # Validate links only
  python url_audit.py --report-only      # Generate reports only
  python url_audit.py --language zh      # Process specific language
  python url_audit.py --verbose          # Verbose output
        """
    )
    
    # Main operation options
    parser.add_argument(
        '--extract-only', 
        action='store_true',
        help='Run only link extraction'
    )
    parser.add_argument(
        '--resolve-only', 
        action='store_true',
        help='Run only URL resolution'
    )
    parser.add_argument(
        '--validate-only', 
        action='store_true',
        help='Run only link validation'
    )
    parser.add_argument(
        '--report-only', 
        action='store_true',
        help='Run only report generation'
    )
    
    # Language option
    parser.add_argument(
        '--language', '-l',
        choices=list(SUPPORTED_LANGUAGES.keys()),
        help='Process specific language only'
    )
    
    # Output options
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    
    # Determine which operation to run
    if args.extract_only:
        run_extraction(args.language, args.verbose)
    elif args.resolve_only:
        run_resolution(args.language, args.verbose)
    elif args.validate_only:
        run_validation(args.language, args.verbose)
    elif args.report_only:
        run_reporting(args.language, args.verbose)
    else:
        # Run complete audit
        run_full_audit(args.language, args.verbose)

if __name__ == "__main__":
    main()
