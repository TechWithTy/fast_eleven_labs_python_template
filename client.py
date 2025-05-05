# backend/apps/eleven_labs/api/client.py

from elevenlabs.client import AsyncElevenLabs as ElevenLabs
from elevenlabs.types import Accent

from app.core.config import settings

print(Accent)
ELEVENLABS_API_KEY = settings.ELEVENLABS_API_KEY

_client = None


def initialize_client(api_key: str) -> None:
    global _client
    _client = ElevenLabs(api_key=api_key)


def get_client() -> ElevenLabs:
    global _client
    if _client is None:
        if not ELEVENLABS_API_KEY:
            raise ValueError(
                "Client not initialized. ELEVENLABS_API_KEY is missing from settings."
            )
        initialize_client(ELEVENLABS_API_KEY)
    return _client
