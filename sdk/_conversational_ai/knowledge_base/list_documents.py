from client import get_client

def list_knowledge_base_documents() -> list[dict]:
    """
    Lists all knowledge base documents.

    Returns:
        list[dict]: The list of knowledge base documents.
    """
    client = get_client()
    return client.conversational_ai.list_knowledge_base_documents()
