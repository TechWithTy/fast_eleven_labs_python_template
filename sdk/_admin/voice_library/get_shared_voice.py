from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

client = get_client()

client.voices.get_shared(
    page_size=1,
    gender="female",
    language="en",
)
