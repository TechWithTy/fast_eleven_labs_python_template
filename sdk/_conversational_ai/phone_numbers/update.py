from client import get_client

def update_phone_number(phone_number_id: str, agent_id: str) -> dict:
    """
    Updates a phone number.

    Args:
        phone_number_id (str): The ID of the phone number to update.
        agent_id (str): The ID of the agent to update the phone number for.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.update_phone_number(phone_number_id=phone_number_id, agent_id=agent_id)
