from typing 
from ...client import get_client

def get_signed_url(agent_id: str) -> dict:
    """
    Retrieves a signed URL for the specified agent.

    Args:
        agent_id (str): The ID of the agent.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.get_signed_url(agent_id=agent_id)
