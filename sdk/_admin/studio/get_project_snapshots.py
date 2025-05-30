
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def get_project_snapshot(project_id: str, project_snapshot_id: str) -> dict:
    """
    Get details of a specific project snapshot.

    Args:
        project_id: The ID of the project.
        project_snapshot_id: The ID of the project snapshot.

    Returns:
        A dictionary containing the snapshot details.
    """
    client = get_client()
    
    return client.studio.chapters.get_chapter_snapshot(
        project_id=project_id,
        chapter_id=project_id,
        chapter_snapshot_id=project_snapshot_id,
    )
