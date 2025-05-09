from typing 
from ...client import get_client


def convert_chapter(project_id: str, chapter_id: str) -> dict:
    """
    Convert a chapter in a studio project.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.

    Returns:
        A dictionary containing the conversion details.
    """
    client = get_client()
    
    return client.studio.chapters.convert(
        project_id=project_id,
        chapter_id=chapter_id,
    )
