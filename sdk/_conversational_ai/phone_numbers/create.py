from client import get_client

def create_phone_number(phone_number: str) -> dict:
    """
    Creates a new phone number.

    Args:
        phone_number (str): The phone number to create.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.conversational_ai.create_phone_number(phone_number=phone_number)
