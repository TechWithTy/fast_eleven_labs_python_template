from typing , Any
from ...client import get_client

def create_agent(conversation_config: dict[str, Any] = {}) -> dict[str, Any]:
    client = get_client()
    response = client.conversational_ai.create_agent(
        conversation_config=conversation_config,
    )
    return response
