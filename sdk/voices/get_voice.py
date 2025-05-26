from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def get_voice(voice_id: str):
    client = get_client()
    response = client.voices.get(voice_id=voice_id)
    return response
