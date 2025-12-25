"""Factory for creating translation providers."""

from typing import Dict, Optional

from .base import TranslationProvider
from .lmstudio import LMStudioProvider
from .openai import OpenAIProvider
from .anthropic import AnthropicProvider


class ProviderFactory:
    """Factory for creating translation providers."""
    
    _providers = {
        "lmstudio": LMStudioProvider,
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
    }
    
    @classmethod
    def get_available_providers(cls) -> list:
        """Get list of available provider names.
        
        Returns:
            List of provider names
        """
        return list(cls._providers.keys())
    
    @classmethod
    def create_provider(cls, provider_name: str, config: Optional[Dict] = None) -> TranslationProvider:
        """Create a translation provider instance.
        
        Args:
            provider_name: Name of the provider (lmstudio, openai, anthropic)
            config: Optional configuration dictionary
        
        Returns:
            TranslationProvider instance
        
        Raises:
            ValueError: If provider name is not recognized
        """
        if config is None:
            config = {}
        
        provider_name_lower = provider_name.lower()
        
        if provider_name_lower not in cls._providers:
            available = ", ".join(cls._providers.keys())
            raise ValueError(
                f"Unknown provider: {provider_name}. "
                f"Available providers: {available}"
            )
        
        provider_class = cls._providers[provider_name_lower]
        return provider_class(config)
    
    @classmethod
    def register_provider(cls, name: str, provider_class: type):
        """Register a custom provider class.
        
        Args:
            name: Provider name
            provider_class: Provider class (must inherit from TranslationProvider)
        """
        if not issubclass(provider_class, TranslationProvider):
            raise TypeError("Provider class must inherit from TranslationProvider")
        cls._providers[name.lower()] = provider_class


def get_provider(provider_name: str, config: Optional[Dict] = None) -> TranslationProvider:
    """Convenience function to get a provider instance.
    
    Args:
        provider_name: Name of the provider
        config: Optional configuration dictionary
    
    Returns:
        TranslationProvider instance
    """
    return ProviderFactory.create_provider(provider_name, config)

