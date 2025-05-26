from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def list_models():
    client = get_client()

    return client.models.get_all()