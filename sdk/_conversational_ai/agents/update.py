from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def update_agent(agent_id: str) -> dict:
    client = get_client()
    response = client.conversational_ai.update_agent(
        agent_id=agent_id,
    )
    return response
