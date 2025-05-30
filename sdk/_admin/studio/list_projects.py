from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def list_studio_projects() -> list[dict]:
    """
    list all studio projects.

    Returns:
        A list of dictionaries containing project details.
    """
    client = get_client()
    
    return client.studio.projects.list()