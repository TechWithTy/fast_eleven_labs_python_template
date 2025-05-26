from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

client = get_client()

client.user.get_subscription()
    