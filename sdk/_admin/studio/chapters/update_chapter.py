from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def update_chapter(project_id: str, chapter_id: str, name: str) -> dict:
    """
    Update a chapter in a studio project.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.
        name: The new name of the chapter.

    Returns:
        A dictionary containing the updated chapter details.
    """
    client = get_client()
    
    return client.studio.chapters.update(
        project_id=project_id,
        chapter_id=chapter_id,
        name=name,
    )
