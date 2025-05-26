from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_secrets() -> list[dict]:
    """
    Retrieves all secrets.

    Returns:
        list[dict]: The list of secrets.
    """
    client = get_client()
    return client.conversational_ai.get_secrets()
