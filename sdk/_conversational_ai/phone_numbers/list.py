from typing  dict
from ...client import get_client

def list_phone_numbers() -> list[dict]:
    """
    Lists all phone numbers.

    Returns:
        list[dict]: The list of phone numbers.
    """
    client = get_client()
    return client.conversational_ai.list_phone_numbers()
