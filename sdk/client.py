"""
Production-grade ElevenLabs client factory for SDK usage.
Loads API key from environment, ensures singleton pattern, and provides type hints.
"""
from typing import Any
import os
from elevenlabs import ElevenLabs
from app.core.config import settings

_client_instance: ElevenLabs | None = None

# ! Important: API key should always come from environment for security
ELEVENLABS_API_KEY = settings.elevenlabs.ELEVENLABS_API_KEY
if not ELEVENLABS_API_KEY:
    raise RuntimeError("ELEVENLABS_API_KEY environment variable is not set. Please set it for secure usage.")

def get_client() -> ElevenLabs:
    """
    Returns a singleton ElevenLabs client instance, configured with the API key from environment.
    """
    global _client_instance
    if _client_instance is None:
        _client_instance = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    return _client_instance
