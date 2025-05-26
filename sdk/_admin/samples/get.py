from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_sample(voice_id: str, sample_id: str) -> dict:
    """
    Retrieves a sample for a specific voice.

    Args:
        voice_id (str): The ID  of the voice.
        sample_id (str): The ID of the sample to retrieve.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.samples.get(voice_id=voice_id, sample_id=sample_id)
