from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_conversation_details(conversation_id: str) -> dict:
    """
    Retrieves details for a conversation.

    Args:
        conversation_id (str): The ID of the conversation.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.get_conversation_details(conversation_id=conversation_id)
