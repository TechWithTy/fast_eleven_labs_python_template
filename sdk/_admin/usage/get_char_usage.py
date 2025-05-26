from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

client = get_client()

client.usage.get_characters_usage_metrics(
    start_unix=1,
    end_unix=1,
)
