"""Anthropic Claude provider for cloud translation."""

import os
from typing import Dict, Optional

try:
    import anthropic
except ImportError:
    anthropic = None

from .base import TranslationProvider


class AnthropicProvider(TranslationProvider):
    """Provider for Anthropic Claude API."""
    
    def __init__(self, config: Dict[str, any]):
        """Initialize Anthropic provider.
        
        Args:
            config: Configuration dict with:
                - api_key: Anthropic API key (required)
                - api_url: Anthropic API URL (default: https://api.anthropic.com/v1)
                - model: Model name (default: claude-3-opus-20240229)
        """
        super().__init__(config)
        self.api_key = config.get("api_key") or os.getenv("ANTHROPIC_API_KEY")
        self.api_url = config.get("api_url") or os.getenv("ANTHROPIC_API_URL", "https://api.anthropic.com")
        self.client = None
        if anthropic and self.api_key:
            self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def validate_config(self) -> bool:
        """Validate Anthropic configuration."""
        if not anthropic:
            raise ImportError(
                "anthropic library is required for Anthropic provider. "
                "Install it with: pip install anthropic"
            )
        
        if not self.api_key:
            raise ValueError(
                "Anthropic API key is required. "
                "Set ANTHROPIC_API_KEY environment variable or use --api-key flag."
            )
        
        if not self.client:
            return False
        
        # Test connection
        try:
            # Lightweight validation - just check if client is initialized
            # Full validation happens on first API call
            return True
        except Exception as e:
            raise ConnectionError(
                f"Failed to initialize Anthropic client. "
                f"Check your API key. Error: {str(e)}"
            )
    
    def get_default_model(self) -> str:
        """Return default model for Anthropic."""
        return "claude-3-opus-20240229"
    
    def translate(self, prompt: str, **kwargs) -> str:
        """Translate using Anthropic API.
        
        Args:
            prompt: Translation prompt
            **kwargs: Additional parameters (model, temperature, max_tokens)
        
        Returns:
            Translated text
        """
        if not self.client:
            raise RuntimeError("Anthropic client not initialized")
        
        model = self.get_model(kwargs.get("model"))
        temperature = self.get_temperature(kwargs.get("temperature"))
        max_tokens = self.get_max_tokens(kwargs.get("max_tokens")) or 4096
        
        try:
            # Anthropic uses a different message format
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                system="You are a professional translator. Translate the given content accurately while preserving all formatting, links, and code blocks.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            if not response.content or len(response.content) == 0:
                raise ValueError("Empty response from Anthropic API")
            
            # Extract text from content blocks
            text_parts = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            
            if not text_parts:
                raise ValueError("No text content in Anthropic API response")
            
            return "\n".join(text_parts).strip()
        
        except Exception as e:
            # Handle rate limits with helpful message
            error_str = str(e).lower()
            if "rate limit" in error_str:
                raise RuntimeError(
                    f"Anthropic rate limit exceeded. Please wait before retrying. "
                    f"Original error: {str(e)}"
                )
            raise RuntimeError(f"Anthropic translation failed: {str(e)}")

