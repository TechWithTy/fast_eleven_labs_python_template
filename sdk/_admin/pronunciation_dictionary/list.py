from client import get_client

def list_pronunciation_dictionaries() -> list[dict]:
    """
    Lists all pronunciation dictionaries.

    Returns:
        list[dict]: The list of pronunciation dictionaries.
    """
    client = get_client()
    return client.pronunciation_dictionary.get_all()
