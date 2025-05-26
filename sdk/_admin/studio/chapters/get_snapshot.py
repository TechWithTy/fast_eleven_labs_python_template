from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def get_snapshot(project_id: str, chapter_id: str, chapter_snapshot_id: str) -> dict:
    """
    Get details of a specific chapter snapshot.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.
        chapter_snapshot_id: The ID of the chapter snapshot.

    Returns:
        A dictionary containing the snapshot details.
    """
    client = get_client()
    
    return client.studio.chapters.get_snapshot(
        project_id=project_id,
        chapter_id=chapter_id,
        chapter_snapshot_id=chapter_snapshot_id,
    )
