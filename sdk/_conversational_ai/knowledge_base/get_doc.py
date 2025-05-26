from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_knowledge_base_document(documentation_id: str) -> dict:
    """
    Retrieves a knowledge base document.

    Args:
        documentation_id (str): The ID of the document.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.get_knowledge_base_document(documentation_id=documentation_id)
