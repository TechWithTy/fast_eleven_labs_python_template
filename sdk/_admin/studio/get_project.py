
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_project(project_id: str) -> dict:
    """
    Get details of a specific studio project.

    Args:
        project_id: The ID of the project to retrieve.

    Returns:
        A dictionary containing the project details.
    """
    client = get_client()
    
    return client.studio.projects.get(
        project_id=project_id,
    )
