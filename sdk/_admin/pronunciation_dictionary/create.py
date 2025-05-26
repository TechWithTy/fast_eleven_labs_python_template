from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def create_pronunciation_dictionary_from_file(name: str, file_path: str) -> dict:
    """
    Creates a pronunciation dictionary from a file.

    Args:
        name (str): The name of the dictionary.
        file_path (str): The path to the file containing the dictionary rules.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    with open(file_path, 'rb') as file:
        return client.pronunciation_dictionary.add_from_file(name=name, file=file)
