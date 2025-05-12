from client import get_client

def update_settings(settings: dict) -> dict:
    """
    Updates the workspace settings.

    Args:
        settings (dict): The new settings to apply.

    Returns:
        dict: The updated workspace settings.
    """
    client = get_client()
    return client.conversational_ai.update_settings(settings=settings)
