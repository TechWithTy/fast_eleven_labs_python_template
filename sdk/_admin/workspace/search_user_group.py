from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def search_user_group(name: str) -> dict:
    """
    Searches for user groups in the workspace.

    Args:
        name (str): The name of the user group to search for.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.search_user_groups(
        name=name,
    )
