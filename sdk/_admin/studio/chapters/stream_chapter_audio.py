from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def stream_chapter_audio(project_id: str, chapter_id: str) -> dict:
    """
    Stream audio for a specific chapter.

    Args:
        project_id: The ID of the project.
        chapter_id: The ID of the chapter.

    Returns:
        A dictionary containing the streaming details.
    """
    client = get_client()   
    
    return client.studio.chapters.stream_audio(
        project_id=project_id,
        chapter_id=chapter_id,
    )