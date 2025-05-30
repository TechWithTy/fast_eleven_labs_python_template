from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def download_history_items(history_item_ids: list):
    client = get_client()
    response = client.history.download(history_item_ids=history_item_ids)
    return response