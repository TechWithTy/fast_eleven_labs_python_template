from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def delete_conversation(conversation_id: str) -> None:
    """
    Deletes a conversation by its ID.

    Args:
        conversation_id (str): The ID of the conversation to delete.
    """
    client = get_client()
    client.conversational_ai.delete_conversation(conversation_id=conversation_id)

delete_conversation(conversation_id="21m00Tcm4TlvDq8ikWAM")
