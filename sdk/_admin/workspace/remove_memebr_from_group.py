from client import get_client

def remove_member_from_group(group_id: str, email: str) -> dict:
    """
    Removes a member from a user group in the workspace.

    Args:
        group_id (str): The ID of the group.
        email (str): The email of the member to remove.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.delete_member_from_user_group(
        group_id=group_id,
        email=email,
    )
