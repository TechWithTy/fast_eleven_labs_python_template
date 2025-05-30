from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def create_pronunciation_dictionaries(project_id: str, pronunciation_dictionary_locators: list[dict]) -> dict:
    """
    Create pronunciation dictionaries for a project.

    Args:
        project_id: The ID of the project.
        pronunciation_dictionary_locators: A list of pronunciation dictionary locators.

    Returns:
        A dictionary containing the pronunciation dictionary details.
    """
    client = get_client()
    
    return client.studio.projects.update_pronunciation_dictionaries(
        project_id=project_id,
        pronunciation_dictionary_locators=pronunciation_dictionary_locators,
    )
