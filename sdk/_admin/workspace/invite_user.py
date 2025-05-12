from client import get_client

def invite_user(email: str) -> dict:
    """
    Invites a user to the workspace.

    Args:
        email (str): The email of the user to invite.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.invite_user(
        email=email,
    )
