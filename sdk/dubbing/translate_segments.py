from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def translate_segments(api_key: str, dubbing_id: str, segments: list):
    client = get_client()

    response = client.dubbing.translate(dubbing_id=dubbing_id, segments=segments)

    return response
