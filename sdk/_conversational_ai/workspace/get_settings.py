from client import get_client

def get_settings() -> dict:
    """
    Retrieves the workspace settings.

    Returns:
        dict: The workspace settings.
    """
    client = get_client()
    return client.conversational_ai.get_settings()
