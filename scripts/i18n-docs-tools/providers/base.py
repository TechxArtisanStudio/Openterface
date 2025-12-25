"""Base class for translation providers."""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class TranslationProvider(ABC):
    """Base class for all translation providers."""
    
    def __init__(self, config: Dict[str, any]):
        """Initialize provider with configuration.
        
        Args:
            config: Provider-specific configuration dictionary
        """
        self.config = config
    
    @abstractmethod
    def translate(self, prompt: str, **kwargs) -> str:
        """Translate text using the provider's API.
        
        Args:
            prompt: The translation prompt to send to the API
            **kwargs: Additional provider-specific parameters
                - model: Model name to use
                - temperature: Temperature for generation
                - max_tokens: Maximum tokens in response
        
        Returns:
            Translated text as string
        
        Raises:
            Exception: If translation fails
        """
        pass
    
    @abstractmethod
    def validate_config(self) -> bool:
        """Validate provider configuration.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        pass
    
    @abstractmethod
    def get_default_model(self) -> str:
        """Return default model for this provider.
        
        Returns:
            Default model name as string
        """
        pass
    
    def get_model(self, override: Optional[str] = None) -> str:
        """Get model to use, with override support.
        
        Args:
            override: Model name override from CLI/config
        
        Returns:
            Model name to use
        """
        return override or self.config.get("model") or self.get_default_model()
    
    def get_temperature(self, override: Optional[float] = None) -> float:
        """Get temperature setting.
        
        Args:
            override: Temperature override from CLI/config
        
        Returns:
            Temperature value (default: 0.3)
        """
        return override or self.config.get("temperature", 0.3)
    
    def get_max_tokens(self, override: Optional[int] = None) -> Optional[int]:
        """Get max tokens setting.
        
        Args:
            override: Max tokens override from CLI/config
        
        Returns:
            Max tokens value or None for auto
        """
        return override or self.config.get("max_tokens")

