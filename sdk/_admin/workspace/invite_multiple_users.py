from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def invite_multiple_users(emails: list[str]) -> dict:
    """
    Invites multiple users to the workspace.

    Args:
        emails (list[str]): The emails of the users to invite.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.invite_multiple_users(
        emails=emails,
    )
