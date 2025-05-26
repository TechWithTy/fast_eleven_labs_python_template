from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def add_member_to_group(group_id: str, email: str) -> dict:
    """
    Adds a member to a user group in the workspace.

    Args:
        group_id (str): The ID of the group.
        email (str): The email of the member to add.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.add_member_to_user_group(
        group_id=group_id,
        email=email,
    )
