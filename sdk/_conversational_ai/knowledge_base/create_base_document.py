from client import get_client

def create_knowledge_base_document(documentation_id: str) -> dict:
    """
    Creates a new knowledge base document.

    Args:
        documentation_id (str): The ID of the document.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.create_knowledge_base_document(documentation_id=documentation_id)
