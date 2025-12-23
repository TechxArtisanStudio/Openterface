#!/usr/bin/env python3
"""
i18n Workflow Management Script

A comprehensive command-line tool for managing i18n workflows in MkDocs projects.
This script combines all the functionality from the i18n_workflow.ipynb notebook
into a single executable command.

Features:
- Generate i18n config from mkdocs.yml
- Audit translation coverage across all languages
- Generate LLM prompts for missing translations
- Display detailed coverage reports
- Quick refresh of entire workflow

Usage:
  python scripts/i18n-docs-tools/workflow.py [command] [options]

Commands:
  audit      Run translation coverage audit
  prompts    Generate LLM prompts for missing translations
  report     Show detailed coverage report
  refresh    Run complete workflow refresh (audit + prompts + report) [DEFAULT]
  guides     Show available translation guides
  status     Show current status and quick actions
  cleanup    Clean up prompts directory

Examples:
  python i18n_workflow.py                    # Runs refresh (default)
  python i18n_workflow.py refresh            # Same as above
  python i18n_workflow.py audit --only-missing
  python i18n_workflow.py prompts --overwrite
  python i18n_workflow.py report
"""

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


class I18nWorkflow:
    """Main class for managing i18n workflow operations."""
    
    def __init__(self, project_root: Optional[str] = None):
        """Initialize the workflow manager."""
        if project_root:
            self.project_root = Path(project_root)
        else:
            # If script is in scripts/i18n-docs-tools/, go up two levels to find project root
            script_dir = Path(__file__).parent
            if script_dir.name == "i18n-docs-tools":
                self.project_root = script_dir.parent.parent
            else:
                self.project_root = Path.cwd()
        
        self.i18n_tools_dir = self.project_root / "scripts" / "i18n-docs-tools"
        self.docs_dir = self.project_root / "docs"
        self.mkdocs_config = self.project_root / "mkdocs.yml"
        self.lang_yml = self.docs_dir / "assets" / "i18n-sites" / "lang.yml"
        self.audit_csv = self.i18n_tools_dir / "i18n_audit.csv"
        self.prompts_dir = self.i18n_tools_dir / "prompts"
        self.guides_dir = self.i18n_tools_dir / "translation_guide"
        
    def get_python_executable(self) -> str:
        """Get the appropriate Python executable (prefer virtual environment)."""
        # Check for virtual environment in common locations
        venv_paths = [
            self.project_root / ".venv" / "bin" / "python",
            self.project_root / "venv" / "bin" / "python",
            Path.home() / ".virtualenvs" / self.project_root.name / "bin" / "python"
        ]
        
        for venv_python in venv_paths:
            if venv_python.exists():
                return str(venv_python)
        
        # Fall back to system Python
        return sys.executable
    
    def run_command(self, cmd: List[str], description: str = "") -> bool:
        """Run a command and return success status."""
        if description:
            print(f"🔄 {description}")
        
        # Replace python executable with the appropriate one
        if cmd[0] == sys.executable:
            cmd[0] = self.get_python_executable()
        
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.stdout:
            print(f"STDOUT: {result.stdout}")
        if result.stderr:
            print(f"STDERR: {result.stderr}")
        
        success = result.returncode == 0
        if success:
            print("✅ Success")
        else:
            print("❌ Failed")
        
        return success
    
    def cleanup_prompts(self) -> bool:
        """Clean up the prompts directory before generating new ones."""
        if not self.prompts_dir.exists():
            return True
        
        try:
            import shutil
            shutil.rmtree(self.prompts_dir)
            print(f"🧹 Cleaned up prompts directory: {self.prompts_dir}")
            return True
        except Exception as e:
            print(f"❌ Failed to clean up prompts directory: {e}")
            return False
    
    
    def run_audit(self, only_missing: bool = False, fail_on_missing: bool = False) -> bool:
        """Run translation coverage audit."""
        cmd = [
            sys.executable,
            str(self.i18n_tools_dir / "audit_translations.py"),
            "--docs", str(self.docs_dir),
            "--config", str(self.lang_yml),
            "--output", str(self.audit_csv)
        ]
        
        if only_missing:
            cmd.append("--only-missing")
        if fail_on_missing:
            cmd.append("--fail-on-missing")
        
        return self.run_command(cmd, "Running translation coverage audit")
    
    def generate_prompts(self, overwrite: bool = False) -> bool:
        """Generate LLM prompts for missing translations."""
        cmd = [
            sys.executable,
            str(self.i18n_tools_dir / "generate_prompts.py"),
            "--docs", str(self.docs_dir),
            "--config", str(self.lang_yml),
            "--output-dir", str(self.prompts_dir),
            "--translation-guide-dir", str(self.guides_dir)
        ]
        
        if overwrite:
            cmd.append("--overwrite")
        
        return self.run_command(cmd, "Generating LLM prompts for missing translations")
    
    def load_coverage_data(self) -> Optional[Tuple[List[str], List[str]]]:
        """Load and analyze coverage data from CSV."""
        if not self.audit_csv.exists():
            print("❌ Audit CSV not found. Please run the audit first.")
            return None
        
        try:
            df = []
            with open(self.audit_csv, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                df = list(reader)
            
            if not df:
                print("❌ No data found in audit CSV")
                return None
            
            # Get language columns (exclude 'group' column)
            lang_cols = [col for col in df[0].keys() if col != 'group']
            
            return df, lang_cols
        except Exception as e:
            print(f"❌ Failed to load coverage data: {e}")
            return None
    
    def show_coverage_summary(self, df: List[Dict], lang_cols: List[str]) -> None:
        """Display coverage summary."""
        print(f"\n📊 Coverage Summary:")
        print(f"Total files: {len(df)}")
        print(f"Languages: {', '.join(lang_cols)}")
        print(f"\nCoverage by language:")
        
        for lang in lang_cols:
            present_count = sum(1 for row in df if row[lang] == '1')
            coverage = (present_count / len(df)) * 100
            missing = len(df) - present_count
            print(f"  {lang}: {coverage:.1f}% ({missing} missing)")
    
    def show_missing_details(self, df: List[Dict], lang_cols: List[str]) -> None:
        """Show detailed information about missing translations."""
        # Find files with missing translations
        missing_files = []
        for row in df:
            missing_langs = [lang for lang in lang_cols if row[lang] == '0']
            if missing_langs:
                missing_files.append((row['group'], missing_langs))
        
        if not missing_files:
            print("🎉 No missing translations found! All files are fully translated.")
            return
        
        print(f"\n📋 Files with Missing Translations ({len(missing_files)} files):")
        print("=" * 60)
        
        for file_name, missing_langs in missing_files:
            present_langs = [lang for lang in lang_cols if lang not in missing_langs]
            
            print(f"\n📄 {file_name}")
            print(f"   ✅ Present: {', '.join(present_langs)}")
            print(f"   ❌ Missing: {', '.join(missing_langs)}")
            
            # Show what files need to be created
            base_name = file_name.replace('.md', '')
            print(f"   📝 Files to create:")
            for lang in missing_langs:
                print(f"      - docs/{base_name}.{lang}.md")
    
    def show_translation_guides(self) -> None:
        """Show available translation guides."""
        if not self.guides_dir.exists():
            print("❌ Translation guides directory not found")
            return
        
        guide_files = list(self.guides_dir.glob('*.md'))
        print(f"\n📚 Available translation guides ({len(guide_files)} files):")
        
        for guide_file in sorted(guide_files):
            size = guide_file.stat().st_size
            print(f"   - {guide_file.name} ({size} bytes)")
    
    def show_prompt_files(self) -> None:
        """Show generated prompt files."""
        if not self.prompts_dir.exists():
            print("❌ Prompts directory not found")
            return
        
        prompt_files = list(self.prompts_dir.glob('*.llm-task.md'))
        print(f"\n🤖 Generated prompt files ({len(prompt_files)} files):")
        
        for prompt_file in sorted(prompt_files):
            size = prompt_file.stat().st_size
            print(f"   - {prompt_file.name} ({size} bytes)")
    
    def quick_refresh(self) -> bool:
        """Run a quick refresh of the entire i18n workflow."""
        print("🔄 Running quick refresh of i18n workflow...")
        
        # Step 0: Clean up prompts directory
        print("\n0️⃣ Cleaning up prompts directory...")
        if not self.cleanup_prompts():
            return False
        
        # Step 1: Run audit
        print("\n1️⃣ Running translation audit...")
        if not self.run_audit():
            return False
        
        # Step 2: Generate prompts
        print("\n2️⃣ Generating LLM prompts...")
        if not self.generate_prompts(overwrite=True):
            return False
        
        print("\n✅ Quick refresh completed!")
        return True
    
    def show_status(self) -> None:
        """Show current status and available actions."""
        print("🎯 i18n Workflow Status")
        print("=" * 30)
        
        # Check file existence
        files_status = {
            "mkdocs.yml": self.mkdocs_config.exists(),
            "lang.yml": self.lang_yml.exists(),
            "audit.csv": self.audit_csv.exists(),
            "prompts/": self.prompts_dir.exists(),
            "guides/": self.guides_dir.exists(),
        }
        
        print("\n📁 File Status:")
        for file_name, exists in files_status.items():
            status = "✅" if exists else "❌"
            print(f"   {status} {file_name}")
        
        # Show quick actions
        print("\n🎯 Quick Actions Available:")
        print("   - refresh: Run complete workflow refresh")
        print("   - audit: Run translation audit")
        print("   - prompts: Generate LLM prompts")
        print("   - report: Show detailed coverage report")
        print("   - guides: Show available translation guides")
        print("   - status: Show this status information")
        print("   - cleanup: Clean up prompts directory")


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="i18n Workflow Management Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "command",
        nargs="?",
        default="refresh",
        choices=["audit", "prompts", "report", "refresh", "guides", "status", "cleanup"],
        help="Command to execute (default: refresh)"
    )
    
    parser.add_argument(
        "--project-root",
        default=None,
        help="Project root directory (default: current directory)"
    )
    
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing files"
    )
    
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing prompt files"
    )
    
    parser.add_argument(
        "--only-missing",
        action="store_true",
        help="Show only files with missing translations"
    )
    
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with error code if missing translations found"
    )
    
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_args()
    
    # Initialize workflow manager
    workflow = I18nWorkflow(args.project_root)
    
    # Execute command
    if args.command == "audit":
        success = workflow.run_audit(
            only_missing=args.only_missing,
            fail_on_missing=args.fail_on_missing
        )
        return 0 if success else 1
    
    elif args.command == "prompts":
        success = workflow.generate_prompts(overwrite=args.overwrite)
        return 0 if success else 1
    
    elif args.command == "report":
        coverage_data = workflow.load_coverage_data()
        if coverage_data:
            df, lang_cols = coverage_data
            workflow.show_coverage_summary(df, lang_cols)
            workflow.show_missing_details(df, lang_cols)
        return 0
    
    elif args.command == "refresh":
        success = workflow.quick_refresh()
        if success:
            # Show report after refresh
            coverage_data = workflow.load_coverage_data()
            if coverage_data:
                df, lang_cols = coverage_data
                workflow.show_coverage_summary(df, lang_cols)
                workflow.show_missing_details(df, lang_cols)
            workflow.show_translation_guides()
            workflow.show_prompt_files()
        return 0 if success else 1
    
    elif args.command == "guides":
        workflow.show_translation_guides()
        return 0
    
    elif args.command == "status":
        workflow.show_status()
        return 0
    
    elif args.command == "cleanup":
        success = workflow.cleanup_prompts()
        return 0 if success else 1
    
    else:
        print(f"Unknown command: {args.command}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
