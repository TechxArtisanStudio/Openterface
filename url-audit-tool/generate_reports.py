#!/usr/bin/env python3
"""
Report Generation Module
Generates comprehensive reports and analysis from validated link data
"""

import logging
from datetime import datetime

import pandas as pd
from config import BASE_URL, OUTPUT_DIR, REPORTS_DIR, SUPPORTED_LANGUAGES

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/generate_reports.log"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


class ReportGenerator:
    def __init__(self):
        self.reports_generated = []
        self.analysis_data = {}

    def load_validation_data(self, language: str = None) -> pd.DataFrame:
        """Load validation data from CSV files"""
        if language:
            csv_file = OUTPUT_DIR / language / "links_validated.csv"
        else:
            csv_file = OUTPUT_DIR / "all_languages_links_validated.csv"

        if not csv_file.exists():
            logger.warning(f"Validation data file not found: {csv_file}")
            return pd.DataFrame()

        df = pd.read_csv(csv_file)
        logger.info(f"Loaded {len(df)} validation records from {csv_file}")
        return df

    def generate_summary_report(self, df: pd.DataFrame) -> str:
        """Generate a comprehensive summary report"""
        report_lines = []
        report_lines.append("# URL Audit Summary Report")
        report_lines.append(
            f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report_lines.append(f"Base URL: {BASE_URL}")
        report_lines.append("")

        # Overall statistics
        total_urls = len(df)
        valid_urls = len(df[df["is_valid"] == True])
        invalid_urls = len(df[df["is_valid"] == False])
        success_rate = (valid_urls / total_urls * 100) if total_urls > 0 else 0

        report_lines.append("## Overall Statistics")
        report_lines.append(f"- **Total URLs**: {total_urls:,}")
        report_lines.append(f"- **Valid URLs**: {valid_urls:,}")
        report_lines.append(f"- **Invalid URLs**: {invalid_urls:,}")
        report_lines.append(f"- **Success Rate**: {success_rate:.1f}%")
        report_lines.append("")

        # Language breakdown
        if "language" in df.columns:
            report_lines.append("## Language Breakdown")
            lang_stats = (
                df.groupby("language").agg({"url": "count", "is_valid": "sum"}).round(2)
            )
            lang_stats.columns = ["Total URLs", "Valid URLs"]
            lang_stats["Success Rate %"] = (
                lang_stats["Valid URLs"] / lang_stats["Total URLs"] * 100
            ).round(1)

            for lang, row in lang_stats.iterrows():
                lang_name = SUPPORTED_LANGUAGES.get(lang, lang)
                report_lines.append(
                    f"- **{lang_name} ({lang})**: {row['Total URLs']} URLs, {row['Success Rate %']:.1f}% valid"
                )
            report_lines.append("")

        # Status code breakdown
        if "status_code" in df.columns:
            status_counts = df["status_code"].value_counts().head(10)
            report_lines.append("## Top HTTP Status Codes")
            for status, count in status_counts.items():
                report_lines.append(f"- **{status}**: {count:,}")
            report_lines.append("")

        # Domain analysis
        if "domain" in df.columns:
            domain_counts = df["domain"].value_counts().head(15)
            report_lines.append("## Top Domains")
            for domain, count in domain_counts.items():
                report_lines.append(f"- **{domain}**: {count:,} URLs")
            report_lines.append("")

        # Error analysis
        error_data = df[df["is_valid"] == False]
        if not error_data.empty and "error_message" in error_data.columns:
            error_counts = error_data["error_message"].value_counts().head(10)
            report_lines.append("## Top Error Messages")
            for error, count in error_counts.items():
                report_lines.append(f"- **{error}**: {count:,}")
            report_lines.append("")

        # Protocol-specific URLs analysis
        if "error_message" in df.columns:
            protocol_skipped = df[
                df["error_message"].str.contains("protocol", na=False)
            ]
            if not protocol_skipped.empty:
                report_lines.append("## Protocol-Specific URLs (Skipped)")
                protocol_counts = protocol_skipped["error_message"].value_counts()
                for protocol_msg, count in protocol_counts.items():
                    report_lines.append(f"- **{protocol_msg}**: {count:,}")
                report_lines.append("")

        # JavaScript redirect analysis
        if "js_redirect_detected" in df.columns:
            js_redirects = df[df["js_redirect_detected"].notna()]
            if not js_redirects.empty:
                report_lines.append("## JavaScript Redirects on Error Pages")
                report_lines.append(
                    f"- **Total URLs with JS redirects**: {len(js_redirects):,}"
                )

                # Count by redirect type
                redirect_types = js_redirects["js_redirect_detected"].value_counts()
                for redirect_type, count in redirect_types.items():
                    report_lines.append(f"- **{redirect_type}**: {count:,}")
                report_lines.append("")

        # Response time analysis
        response_times = df[df["response_time"].notna()]["response_time"]
        if not response_times.empty:
            report_lines.append("## Response Time Analysis")
            report_lines.append(f"- **Average**: {response_times.mean():.3f}s")
            report_lines.append(f"- **Median**: {response_times.median():.3f}s")
            report_lines.append(
                f"- **95th Percentile**: {response_times.quantile(0.95):.3f}s"
            )
            report_lines.append(f"- **Max**: {response_times.max():.3f}s")
            report_lines.append("")

        # Usage frequency analysis
        if "usage_count" in df.columns:
            usage_stats = (
                df.groupby("usage_count").size().sort_index(ascending=False).head(10)
            )
            report_lines.append("## Most Frequently Used URLs")
            for usage_count, url_count in usage_stats.items():
                report_lines.append(
                    f"- **Used {usage_count} times**: {url_count} unique URLs"
                )
            report_lines.append("")

        return "\n".join(report_lines)

    def generate_broken_links_report(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generate detailed broken links report"""
        broken_links = df[df["is_valid"] == False].copy()

        if broken_links.empty:
            logger.info("No broken links found")
            return pd.DataFrame()

        # Sort by error message and usage count
        broken_links = broken_links.sort_values(
            ["error_message", "usage_count"], ascending=[True, False]
        )

        logger.info(f"Found {len(broken_links)} broken links")
        return broken_links

    def generate_url_frequency_analysis(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generate URL frequency analysis"""
        if "usage_count" in df.columns:
            # Sort by usage count
            frequency_analysis = df.sort_values("usage_count", ascending=False)

            # Add some additional analysis
            frequency_analysis["is_high_traffic"] = (
                frequency_analysis["usage_count"] >= 5
            )
            frequency_analysis["is_medium_traffic"] = (
                frequency_analysis["usage_count"] >= 2
            ) & (frequency_analysis["usage_count"] < 5)
            frequency_analysis["is_low_traffic"] = (
                frequency_analysis["usage_count"] == 1
            )

            return frequency_analysis
        else:
            return df

    def generate_domain_analysis(self, df: pd.DataFrame) -> pd.DataFrame:
        """Generate domain-level analysis"""
        if "domain" not in df.columns:
            return pd.DataFrame()

        domain_analysis = (
            df.groupby("domain")
            .agg(
                {
                    "url": "count",
                    "is_valid": "sum",
                    "usage_count": "sum",
                    "response_time": "mean",
                }
            )
            .round(3)
        )

        domain_analysis.columns = [
            "Total URLs",
            "Valid URLs",
            "Total Usage",
            "Avg Response Time",
        ]
        domain_analysis["Success Rate %"] = (
            domain_analysis["Valid URLs"] / domain_analysis["Total URLs"] * 100
        ).round(1)
        domain_analysis = domain_analysis.sort_values("Total Usage", ascending=False)

        return domain_analysis

    def save_reports(
        self,
        summary_report: str,
        broken_links_df: pd.DataFrame,
        frequency_df: pd.DataFrame,
        domain_df: pd.DataFrame,
    ):
        """Save all generated reports"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save summary report
        summary_file = REPORTS_DIR / f"url_audit_summary_{timestamp}.md"
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary_report)
        logger.info(f"Saved summary report to {summary_file}")

        # Save broken links report
        if not broken_links_df.empty:
            broken_file = REPORTS_DIR / f"broken_links_{timestamp}.csv"
            broken_links_df.to_csv(broken_file, index=False, encoding="utf-8")
            logger.info(f"Saved broken links report to {broken_file}")

        # Save frequency analysis
        if not frequency_df.empty:
            frequency_file = REPORTS_DIR / f"url_frequency_analysis_{timestamp}.csv"
            frequency_df.to_csv(frequency_file, index=False, encoding="utf-8")
            logger.info(f"Saved frequency analysis to {frequency_file}")

        # Save domain analysis
        if not domain_df.empty:
            domain_file = REPORTS_DIR / f"domain_analysis_{timestamp}.csv"
            domain_df.to_csv(domain_file, index=False, encoding="utf-8")
            logger.info(f"Saved domain analysis to {domain_file}")

        # Create latest symlinks (if on Unix-like systems)
        try:
            latest_summary = REPORTS_DIR / "latest_summary.md"
            if latest_summary.exists():
                latest_summary.unlink()
            latest_summary.symlink_to(summary_file.name)
        except OSError:
            pass  # Skip if symlinks not supported

        self.reports_generated = [
            summary_file,
            broken_file if not broken_links_df.empty else None,
            frequency_file if not frequency_df.empty else None,
            domain_file if not domain_df.empty else None,
        ]

    def print_report_summary(self, summary_report: str, broken_count: int):
        """Print a summary of generated reports"""
        print("\n" + "=" * 60)
        print("REPORT GENERATION SUMMARY")
        print("=" * 60)

        # Extract key stats from summary report
        lines = summary_report.split("\n")
        for line in lines:
            if line.startswith("- **Total URLs**"):
                print(f"Total URLs analyzed: {line.split(':')[1].strip()}")
            elif line.startswith("- **Success Rate**"):
                print(f"Success rate: {line.split(':')[1].strip()}")

        print(f"Broken links found: {broken_count}")
        print(f"Reports generated: {len([r for r in self.reports_generated if r])}")

        print("\nGenerated files:")
        for report_file in self.reports_generated:
            if report_file:
                print(f"  - {report_file}")

        print(f"\nAll reports saved to: {REPORTS_DIR}")


def main():
    """Main function to generate reports"""
    print("Starting report generation...")

    generator = ReportGenerator()

    # Load validation data
    df = generator.load_validation_data()

    if df.empty:
        print("No validation data found. Please run validate_links.py first.")
        return

    # Generate reports
    logger.info("Generating summary report...")
    summary_report = generator.generate_summary_report(df)

    logger.info("Generating broken links report...")
    broken_links_df = generator.generate_broken_links_report(df)

    logger.info("Generating frequency analysis...")
    frequency_df = generator.generate_url_frequency_analysis(df)

    logger.info("Generating domain analysis...")
    domain_df = generator.generate_domain_analysis(df)

    # Save all reports
    generator.save_reports(summary_report, broken_links_df, frequency_df, domain_df)

    # Print summary
    generator.print_report_summary(summary_report, len(broken_links_df))

    print(f"\nReport generation completed! Check the 'reports' directory for results.")


if __name__ == "__main__":
    main()
