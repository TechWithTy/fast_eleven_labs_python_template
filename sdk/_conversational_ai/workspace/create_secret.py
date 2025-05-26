from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def create_secret(name: str, value: str) -> dict:
    """
    Creates a new secret.

    Args:
        name (str): The name of the secret.
        value (str): The value of the secret.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.create_secret(name=name, value=value)
