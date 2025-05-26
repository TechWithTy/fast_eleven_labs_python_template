
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def convert_project(project_id: str) -> dict:
    """
    Convert a studio project.

    Args:
        project_id: The ID of the project to convert.

    Returns:
        A dictionary containing the conversion details.
    """
    client = get_client()
    
    return client.studio.projects.convert(
        project_id=project_id,
    )
