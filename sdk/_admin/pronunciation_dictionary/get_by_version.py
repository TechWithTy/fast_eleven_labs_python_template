from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_pronunciation_dictionary_by_version(dictionary_id: str, version_id: str) -> dict:
    """
    Retrieves a pronunciation dictionary by version.

    Args:   
        dictionary_id (str): The ID of the dictionary.
        version_id (str): The version ID of the dictionary.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.pronunciation_dictionary.get_by_version(dictionary_id=dictionary_id, version_id=version_id)