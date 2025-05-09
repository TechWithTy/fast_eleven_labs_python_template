from typing 
from ...client import get_client

def get_agent(agent_id: str) -> dict:
    client = get_client()
    response = client.conversational_ai.get_agent(agent_id=agent_id)
    return response