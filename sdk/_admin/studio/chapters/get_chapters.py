from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def get_chapters(project_id: str, chapter_id: str) -> dict:
    """
    Get details of a specific chapter.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.

    Returns:
        A dictionary containing the chapter details.
    """
    client = get_client()
    
    return client.studio.chapters.get(
        project_id=project_id,
        chapter_id=chapter_id,
    )
