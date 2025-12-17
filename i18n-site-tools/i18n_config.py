"""
Shared i18n configuration loader for all static page generators.
Reads from docs/assets/i18n-sites/i18n.yml as single source of truth.
"""

import yaml
from pathlib import Path
from typing import Dict, List


class I18nConfig:
    """Centralized i18n configuration."""
    
    def __init__(self, config_path: Path = None):
        if config_path is None:
            # Default path relative to project root
            script_dir = Path(__file__).parent
            config_path = script_dir.parent / "docs" / "assets" / "i18n-sites" / "i18n.yml"
        
        self.config_path = config_path
        self._config = self._load_config()
    
    def _load_config(self) -> Dict:
        """Load YAML configuration."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"i18n config not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    @property
    def languages(self) -> List[str]:
        """Get list of supported languages."""
        return self._config.get('languages', [])
    
    @property
    def default_language(self) -> str:
        """Get default language."""
        return self._config.get('default_language', 'en')
    
    def validate_json_languages(self, json_languages: List[str], source_name: str) -> None:
        """
        Validate that JSON file has all required languages.
        Warns if languages are missing but doesn't fail.
        """
        yaml_set = set(self.languages)
        json_set = set(json_languages)
        
        missing = yaml_set - json_set
        extra = json_set - yaml_set
        
        if missing:
            print(f"⚠️  Warning: {source_name} missing languages: {', '.join(sorted(missing))}")
            print(f"   Will only generate pages for: {', '.join(sorted(json_set & yaml_set))}")
        
        if extra:
            print(f"ℹ️  Info: {source_name} has extra languages not in i18n.yml: {', '.join(sorted(extra))}")
    
    def generate_hreflang_html(self, base_url: str = "{{ config.site_url }}") -> str:
        """
        Generate complete hreflang HTML file content for all configured languages.
        
        Args:
            base_url: Base URL template (Jinja2 compatible)
        
        Returns:
            Complete HTML content for hreflang.html partial
        """
        links = []
        
        # Add link for each language
        for lang in self.languages:
            if lang == self.default_language:
                href = f"{base_url}/"
            else:
                href = f"{base_url}/{lang}/"
            
            links.append(f'<link rel="alternate" hreflang="{lang}" href="{href}">')
        
        # Add x-default (fallback to default language)
        links.append(f'<link rel="alternate" hreflang="x-default" href="{base_url}/">')
        
        # Add header comment
        header = "<!-- hreflang links - Auto-generated from i18n.yml -->"
        
        return header + '\n' + '\n'.join(links) + '\n'
    
    def generate_hreflang_file(self, output_dir: Path) -> None:
        """
        Generate docs/partials/hreflang.html file.
        
        Args:
            output_dir: Directory where partials are stored (docs/partials)
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / "hreflang.html"
        
        html_content = self.generate_hreflang_html()
        output_path.write_text(html_content, encoding='utf-8')
        
        print(f"✅ Generated: {output_path}")

