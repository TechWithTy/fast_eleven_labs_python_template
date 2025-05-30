from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def post_conversation_feedback(conversation_id: str, feedback: str) -> dict:
    """
    Posts feedback for a conversation.

    Args:
        conversation_id (str): The ID of the conversation.
        feedback (str): The feedback to post (e.g., 'like').

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.post_conversation_feedback(
        conversation_id=conversation_id,
        feedback=feedback,
    )
