"""OpenAI provider for cloud translation."""

import os
from typing import Dict, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base import TranslationProvider


class OpenAIProvider(TranslationProvider):
    """Provider for OpenAI API."""
    
    def __init__(self, config: Dict[str, any]):
        """Initialize OpenAI provider.
        
        Args:
            config: Configuration dict with:
                - api_key: OpenAI API key (required)
                - api_url: OpenAI API URL (default: https://api.openai.com/v1)
                - model: Model name (default: gpt-4-turbo-preview)
        """
        super().__init__(config)
        self.api_key = config.get("api_key") or os.getenv("OPENAI_API_KEY")
        self.api_url = config.get("api_url") or os.getenv("OPENAI_API_URL", "https://api.openai.com/v1")
        self.client = None
        if OpenAI and self.api_key:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.api_url
            )
    
    def validate_config(self) -> bool:
        """Validate OpenAI configuration."""
        if not OpenAI:
            raise ImportError(
                "openai library is required for OpenAI provider. "
                "Install it with: pip install openai"
            )
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API key is required. "
                "Set OPENAI_API_KEY environment variable or use --api-key flag."
            )
        
        if not self.client:
            raise RuntimeError(
                "OpenAI client not initialized. "
                "This should not happen - please report this issue."
            )
        
        # Test connection with a lightweight request
        try:
            self.client.models.list()
            return True
        except Exception as e:
            raise ConnectionError(
                f"Failed to connect to OpenAI API. "
                f"Check your API key and network connection. "
                f"Error: {str(e)}"
            )
    
    def get_default_model(self) -> str:
        """Return default model for OpenAI."""
        return "gpt-4-turbo-preview"
    
    def translate(self, prompt: str, **kwargs) -> str:
        """Translate using OpenAI API.
        
        Args:
            prompt: Translation prompt
            **kwargs: Additional parameters (model, temperature, max_tokens)
        
        Returns:
            Translated text
        """
        if not self.client:
            raise RuntimeError("OpenAI client not initialized")
        
        model = self.get_model(kwargs.get("model"))
        temperature = self.get_temperature(kwargs.get("temperature"))
        max_tokens = self.get_max_tokens(kwargs.get("max_tokens"))
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a professional translator. Translate the given content accurately while preserving all formatting, links, and code blocks."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            if not response.choices or not response.choices[0].message:
                raise ValueError("Empty response from OpenAI API")
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            # Handle rate limits with helpful message
            error_str = str(e).lower()
            if "rate limit" in error_str:
                raise RuntimeError(
                    f"OpenAI rate limit exceeded. Please wait before retrying. "
                    f"Original error: {str(e)}"
                )
            raise RuntimeError(f"OpenAI translation failed: {str(e)}")

