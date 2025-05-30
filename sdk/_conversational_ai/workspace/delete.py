from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def delete_secret(secret_id: str) -> dict:
    """
    Deletes a secret.

    Args:
        secret_id (str): The ID of the secret to delete.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.delete_secret(secret_id=secret_id)
