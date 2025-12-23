"""
Shared i18n configuration loader that reads directly from lang.yml.
Reads from docs/assets/i18n-sites/lang.yml as single source of truth.
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional


def try_load_yaml(path: Path) -> Optional[dict]:
    """Load YAML file with permissive loader for custom tags."""
    try:
        # Create a permissive loader that treats unknown python/name tags as plain strings
        class PermissiveLoader(yaml.SafeLoader):
            pass

        def construct_python_name(loader, suffix, node):
            # Return the referenced name as a simple string
            return suffix

        yaml.add_multi_constructor(
            "tag:yaml.org,2002:python/name:", construct_python_name, Loader=PermissiveLoader
        )

        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=PermissiveLoader) or {}
    except FileNotFoundError:
        return None
    except Exception:
        return None


def extract_languages_from_lang_yml(lang_data: List[dict]) -> List[str]:
    """Extract language codes from lang.yml data, filtering by build: true."""
    languages: List[str] = []
    
    if not isinstance(lang_data, list):
        return languages
    
    for lang_entry in lang_data:
        if isinstance(lang_entry, dict):
            locale = lang_entry.get("locale")
            if not locale:
                continue
            
            # Check if language should be built
            build = lang_entry.get("build")
            if build is False:
                continue
            
            languages.append(str(locale))
    
    return languages


def get_default_language(mkdocs_path: Path) -> str:
    """Get default language from mkdocs.yml theme.language, fallback to 'en'."""
    mkdocs_data = try_load_yaml(mkdocs_path)
    if not mkdocs_data:
        return "en"
    
    theme = mkdocs_data.get("theme") or {}
    if isinstance(theme, dict):
        lang = theme.get("language")
        if isinstance(lang, str) and lang.strip():
            return lang.strip()
    
    return "en"


class I18nConfig:
    """Centralized i18n configuration that reads from lang.yml directly."""
    
    def __init__(self, lang_yml_path: Optional[Path] = None, mkdocs_path: Optional[Path] = None):
        """
        Initialize i18n configuration.
        
        Args:
            lang_yml_path: Path to lang.yml (default: docs/assets/i18n-sites/lang.yml)
            mkdocs_path: Path to mkdocs.yml (default: mkdocs.yml in project root)
        """
        if lang_yml_path is None:
            # Default path relative to project root
            script_dir = Path(__file__).parent
            project_root = script_dir.parent.parent
            lang_yml_path = project_root / "docs" / "assets" / "i18n-sites" / "lang.yml"
        
        if mkdocs_path is None:
            script_dir = Path(__file__).parent
            project_root = script_dir.parent.parent
            mkdocs_path = project_root / "mkdocs.yml"
        
        self.lang_yml_path = lang_yml_path
        self.mkdocs_path = mkdocs_path
        self._lang_data = self._load_lang_yml()
        self._languages = extract_languages_from_lang_yml(self._lang_data)
        self._default_language = get_default_language(mkdocs_path)
        
        # Ensure default language is in the languages list
        if self._default_language not in self._languages:
            self._languages.insert(0, self._default_language)
    
    def _load_lang_yml(self) -> List[dict]:
        """Load lang.yml file."""
        if not self.lang_yml_path.exists():
            raise FileNotFoundError(f"lang.yml not found: {self.lang_yml_path}")
        
        data = try_load_yaml(self.lang_yml_path)
        if not data:
            raise ValueError(f"Failed to load lang.yml from: {self.lang_yml_path}")
        
        if not isinstance(data, list):
            raise ValueError(f"lang.yml must contain a list of language entries")
        
        return data
    
    @property
    def languages(self) -> List[str]:
        """Get list of supported language codes (with build: true)."""
        return self._languages.copy()
    
    @property
    def default_language(self) -> str:
        """Get default language code."""
        return self._default_language
    
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
            print(f"ℹ️  Info: {source_name} has extra languages not in lang.yml: {', '.join(sorted(extra))}")
    
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
        header = "<!-- hreflang links - Auto-generated from lang.yml -->"
        
        return header + '\n' + '\n'.join(links) + '\n'
    
    def generate_hreflang_file(self, output_dir: Path) -> None:
        """
        Generate hreflang.html file in docs/overrides/partials/.
        
        Args:
            output_dir: Base output directory (e.g., docs/overrides)
        """
        # Create partials subdirectory in overrides (MkDocs template search path)
        partials_dir = output_dir / "partials"
        partials_dir.mkdir(parents=True, exist_ok=True)
        output_path = partials_dir / "hreflang.html"
        
        html_content = self.generate_hreflang_html()
        output_path.write_text(html_content, encoding='utf-8')
        
        print(f"✅ Generated: {output_path}")

