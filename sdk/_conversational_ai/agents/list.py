from typing import Any
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_agents() -> dict[str, Any]:
    client = get_client()
    return client.conversational_ai.get_agents()
