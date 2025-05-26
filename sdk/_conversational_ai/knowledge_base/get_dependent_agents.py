from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_knowledge_base_dependent_agents(documentation_id: str) -> list[dict]:
    """
    Retrieves the list of agents dependent on a knowledge base document.

    Args:
        documentation_id (str): The ID of the document.

    Returns:
        list[dict]: The list of dependent agents.
    """
    client = get_client()
    return client.conversational_ai.get_knowledge_base_dependent_agents(documentation_id=documentation_id)

# Example usage:
# get_knowledge_base_dependent_agents("21m00Tcm4TlvDq8ikWAM")
