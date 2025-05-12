from client import get_client

def delete_invite(email: str) -> dict:
    """
    Deletes an existing invitation.

    Args:
        email (str): The email of the user to delete the invitation for.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.delete_existing_invitation(
        email=email,
    )
