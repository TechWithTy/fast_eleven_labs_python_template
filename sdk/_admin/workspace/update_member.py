from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def update_member(email: str) -> dict:
    """
    Updates a member in the workspace.

    Args:
        email (str): The email of the member to update.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.update_member(
        email=email,
    )
