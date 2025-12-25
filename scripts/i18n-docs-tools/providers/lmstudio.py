"""LM Studio provider for local translation."""

import os
from typing import Dict, Optional

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from .base import TranslationProvider


class LMStudioProvider(TranslationProvider):
    """Provider for LM Studio local API (OpenAI-compatible)."""
    
    def __init__(self, config: Dict[str, any]):
        """Initialize LM Studio provider.
        
        Args:
            config: Configuration dict with:
                - api_url: LM Studio API URL (default: http://localhost:1234/v1)
                - api_key: Not required for LM Studio
                - model: Model name (optional)
        """
        super().__init__(config)
        self.api_url = config.get("api_url") or os.getenv("LM_STUDIO_API_URL", "http://localhost:1234/v1")
        self.client = None
        if OpenAI:
            self.client = OpenAI(
                base_url=self.api_url,
                api_key="not-needed"  # LM Studio doesn't require a real API key
            )
    
    def validate_config(self) -> bool:
        """Validate LM Studio configuration."""
        if not OpenAI:
            raise ImportError(
                "openai library is required for LM Studio provider. "
                "Install it with: pip install openai"
            )
        
        if not self.client:
            raise RuntimeError(
                "LM Studio client not initialized. "
                "This should not happen - please report this issue."
            )
        
        # Test connection
        try:
            # Try to list models (lightweight check)
            # This will fail if LM Studio is not running
            self.client.models.list()
            return True
        except Exception as e:
            raise ConnectionError(
                f"Failed to connect to LM Studio at {self.api_url}. "
                f"Make sure LM Studio is running and the API server is enabled. "
                f"Error: {str(e)}"
            )
    
    def get_default_model(self) -> str:
        """Return default model for LM Studio."""
        # Try to get the first available model
        try:
            if self.client:
                models = self.client.models.list()
                if models.data:
                    return models.data[0].id
        except Exception:
            pass
        # Fallback
        return "local-model"
    
    def translate(self, prompt: str, **kwargs) -> str:
        """Translate using LM Studio API.
        
        Args:
            prompt: Translation prompt
            **kwargs: Additional parameters (model, temperature, max_tokens)
        
        Returns:
            Translated text
        """
        if not self.client:
            raise RuntimeError("LM Studio client not initialized")
        
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
                raise ValueError("Empty response from LM Studio API")
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            raise RuntimeError(f"LM Studio translation failed: {str(e)}")

