"""
Shared i18n configuration loader for all static page generators.
Reads from docs/assets/i18n-sites/lang.yml as single source of truth.
"""

import sys
from pathlib import Path

# Import from shared i18n utilities
sys.path.insert(0, str(Path(__file__).parent.parent / "i18n-shared"))
from lang_loader import I18nConfig

# Re-export for backward compatibility
__all__ = ['I18nConfig']

