from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def delete_chapter(project_id: str, chapter_id: str) -> dict:
    """
    Delete a chapter from a studio project.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.

    Returns:
        A dictionary containing the deletion details.
    """
    client = get_client()
    
    return client.studio.chapters.delete(
        project_id=project_id,
        chapter_id=chapter_id,
    )
