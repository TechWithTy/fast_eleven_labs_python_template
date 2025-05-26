from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def create_chapter(project_id: str, name: str) -> dict:
    """
    Create a new chapter in a studio project.

    Args:
        project_id: The ID of the project.
        name: The name of the chapter.

    Returns:
        A dictionary containing the chapter details.
    """
    client = get_client()
    
    return client.studio.chapters.create(
        project_id=project_id,
        name=name,
    )
