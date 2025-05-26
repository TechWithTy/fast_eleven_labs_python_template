from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def delete_agent(agent_id: str) -> dict:
    client = get_client()
    response = client.conversational_ai.delete_agent(agent_id=agent_id)
    return response
