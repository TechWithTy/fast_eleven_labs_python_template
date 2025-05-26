from app.core.third_party_integrations.eleven_labs_home.sdk import client
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def create_voice_clone(name, files):
    client = get_client()

    response = client.voices.add(name=name, files=files)

    return response
