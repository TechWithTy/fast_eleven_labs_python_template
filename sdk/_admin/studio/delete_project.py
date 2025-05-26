
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def delete_studio_project(project_id: str) -> dict:
    """
    Delete a studio project.

    Args:
        project_id: The ID of the project to delete.

    Returns:
        A dictionary containing the deletion details.
    """
    client = get_client()
    
    return client.studio.projects.delete(
        project_id=project_id,
    )
