from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def create_avatar(agent_id: str) -> dict:
    """
    Creates an avatar for the specified agent.

    Args:
        agent_id (str): The ID of the agent to create the avatar for.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.post_agent_avatar(agent_id=agent_id)
    