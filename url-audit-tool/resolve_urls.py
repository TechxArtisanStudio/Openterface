#!/usr/bin/env python3
"""
URL Resolution Module
Converts relative URLs to absolute URLs and handles language-specific paths
"""

import logging
from typing import Dict, List, Tuple
from urllib.parse import urlparse

import pandas as pd
from config import BASE_URL, OUTPUT_DIR, SUPPORTED_LANGUAGES
from tqdm import tqdm

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("logs/resolve_urls.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class URLResolver:
    def __init__(self):
        self.resolved_links = []
        self.resolution_stats = {
            "total_processed": 0,
            "relative_resolved": 0,
            "already_absolute": 0,
            "mkdocs_variables": 0,
            "invalid_urls": 0,
        }

    def is_absolute_url(self, url: str) -> bool:
        """Check if URL is already absolute"""
        return url.startswith(("http://", "https://", "//"))

    def is_mkdocs_variable(self, url: str) -> bool:
        """Check if URL contains MkDocs template variables"""
        return "{{" in url and "}}" in url

    def is_protocol_specific_url(self, url: str) -> bool:
        """Check if URL is protocol-specific (mailto:, tel:, etc.)"""
        protocols = ["mailto:", "tel:", "sms:", "ftp:", "file:", "javascript:", "data:"]
        return any(url.lower().startswith(protocol) for protocol in protocols)

    def has_language_prefix(self, url: str) -> bool:
        """Check if URL already has a language prefix"""
        if not url.startswith("/"):
            return False

        # Check for language codes at the beginning of the path
        for lang_code in SUPPORTED_LANGUAGES.keys():
            if url.startswith(f"/{lang_code}/") or url == f"/{lang_code}":
                return True
        return False

    def clean_url(self, url: str) -> str:
        """Clean URL by removing fragments and query parameters if needed"""
        # Remove common markdown-specific fragments
        url = url.split("#")[0]  # Remove fragments for now

        # Remove trailing slashes from paths (except root)
        if (
            url.endswith("/")
            and url != "/"
            and not url.startswith(("http://", "https://"))
        ):
            url = url[:-1]

        return url

    def resolve_relative_url(self, url: str, language: str = "en") -> str:
        """Resolve relative URL to absolute URL with language prefix"""
        if self.is_absolute_url(url):
            return url

        if self.is_mkdocs_variable(url):
            # Keep MkDocs variables as-is for now
            return url

        if self.is_protocol_specific_url(url):
            # Keep protocol-specific URLs as-is (mailto:, tel:, etc.)
            return url

        # Clean the URL
        clean_url = self.clean_url(url)

        # Note: We no longer add language prefixes to root-level paths

        # Handle different relative URL patterns
        if clean_url.startswith("/"):
            # Absolute path from root - don't add language prefix for root-level paths
            # This handles cases like /playstore, /appstore, /app, /flathub
            resolved = f"{BASE_URL}{clean_url}"
        else:
            # Relative path - this is more complex and context-dependent
            # For now, treat as absolute path from root
            clean_url = f"/{clean_url}" if not clean_url.startswith("/") else clean_url
            resolved = f"{BASE_URL}{clean_url}"

        return resolved

    def extract_domain_and_path(self, url: str) -> Tuple[str, str]:
        """Extract domain and path from URL"""
        if self.is_mkdocs_variable(url):
            return "template_variable", url

        if self.is_protocol_specific_url(url):
            # Extract protocol and return it as domain
            protocol = url.split(":")[0]
            return f"{protocol}_protocol", url

        try:
            parsed = urlparse(url)
            domain = parsed.netloc or "relative"
            path = parsed.path or "/"
            return domain, path
        except Exception:
            return "invalid", url

    def process_link(self, link: Dict) -> Dict:
        """Process a single link and resolve its URL"""
        raw_url = link["raw_url"]
        language = link["language"]

        # Create resolved link dictionary
        resolved_link = link.copy()

        # Resolve the URL
        if self.is_absolute_url(raw_url):
            resolved_url = raw_url
            self.resolution_stats["already_absolute"] += 1
        elif self.is_mkdocs_variable(raw_url):
            resolved_url = raw_url
            self.resolution_stats["mkdocs_variables"] += 1
        elif self.is_protocol_specific_url(raw_url):
            resolved_url = raw_url
            self.resolution_stats["mkdocs_variables"] += 1  # Count as special case
        else:
            resolved_url = self.resolve_relative_url(raw_url, language)
            self.resolution_stats["relative_resolved"] += 1

        # Generate full URL (same as resolved_url for now)
        full_url = resolved_url

        # Extract domain and path
        domain, path = self.extract_domain_and_path(resolved_url)

        # Add resolved information
        resolved_link.update(
            {
                "resolved_url": resolved_url,
                "full_url": full_url,
                "domain": domain,
                "path": path,
            }
        )

        self.resolution_stats["total_processed"] += 1
        return resolved_link

    def load_extracted_links(self, language: str = None) -> List[Dict]:
        """Load extracted links from CSV files"""
        links = []

        if language:
            # Load specific language
            csv_file = OUTPUT_DIR / language / "links_extracted.csv"
            if csv_file.exists():
                df = pd.read_csv(csv_file)
                links = df.to_dict("records")
                logger.info(f"Loaded {len(links)} links for language: {language}")
            else:
                logger.warning(
                    f"No extracted links file found for language: {language}"
                )
        else:
            # Load all languages
            for lang in SUPPORTED_LANGUAGES.keys():
                csv_file = OUTPUT_DIR / lang / "links_extracted.csv"
                if csv_file.exists():
                    df = pd.read_csv(csv_file)
                    lang_links = df.to_dict("records")
                    links.extend(lang_links)
                    logger.info(f"Loaded {len(lang_links)} links for language: {lang}")

        return links

    def save_resolved_links(self, links: List[Dict]):
        """Save resolved links to CSV files organized by language"""
        if not links:
            logger.warning("No links to save")
            return

        # Group links by language
        links_by_language = {}
        for link in links:
            lang = link["language"]
            if lang not in links_by_language:
                links_by_language[lang] = []
            links_by_language[lang].append(link)

        # Save CSV for each language
        for language, lang_links in links_by_language.items():
            output_file = OUTPUT_DIR / language / "links_resolved.csv"

            df = pd.DataFrame(lang_links)
            df.to_csv(output_file, index=False, encoding="utf-8")

            logger.info(
                f"Saved {len(lang_links)} resolved links for {language} to {output_file}"
            )

        # Save combined results
        combined_file = OUTPUT_DIR / "all_languages_links_resolved.csv"
        df_all = pd.DataFrame(links)
        df_all.to_csv(combined_file, index=False, encoding="utf-8")

        logger.info(f"Saved {len(links)} total resolved links to {combined_file}")

        # Print summary statistics
        self.print_summary(links_by_language)

    def print_summary(self, links_by_language: Dict[str, List[Dict]]):
        """Print summary statistics"""
        print("\n" + "=" * 60)
        print("URL RESOLUTION SUMMARY")
        print("=" * 60)
        print(f"Total links processed: {self.resolution_stats['total_processed']}")
        print(f"Already absolute URLs: {self.resolution_stats['already_absolute']}")
        print(f"Relative URLs resolved: {self.resolution_stats['relative_resolved']}")
        print(f"MkDocs variables found: {self.resolution_stats['mkdocs_variables']}")
        print(f"Invalid URLs: {self.resolution_stats['invalid_urls']}")

        print("\nBy Language:")
        for language, links in links_by_language.items():
            external_count = sum(1 for link in links if link["is_external"])
            relative_count = sum(1 for link in links if not link["is_external"])
            print(
                f"  {language}: {len(links)} links ({external_count} external, {relative_count} relative)"
            )

        print("\nBy Domain:")
        all_links = [link for links in links_by_language.values() for link in links]
        domains = {}
        for link in all_links:
            domain = link["domain"]
            domains[domain] = domains.get(domain, 0) + 1

        for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True)[
            :10
        ]:
            print(f"  {domain}: {count}")

        if len(domains) > 10:
            print(f"  ... and {len(domains) - 10} more domains")


def main():
    """Main function to run URL resolution"""
    print("Starting URL resolution...")

    resolver = URLResolver()

    # Load extracted links
    links = resolver.load_extracted_links()

    if not links:
        print("No extracted links found. Please run extract_links.py first.")
        return

    # Process links with progress bar
    resolved_links = []
    for link in tqdm(links, desc="Resolving URLs"):
        resolved_link = resolver.process_link(link)
        resolved_links.append(resolved_link)

    # Save results
    resolver.save_resolved_links(resolved_links)

    print(f"\nURL resolution completed! Check the 'data' directory for results.")


if __name__ == "__main__":
    main()
