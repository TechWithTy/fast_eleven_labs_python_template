from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def list_chapters(project_id: str) -> list[dict]:
    """
    list all chapters in a studio project.

    Args:
        project_id: The ID of the project.

    Returns:
        A list of dictionaries containing chapter details.
    """
    client = get_client()
    
    return client.studio.chapters.list(
        project_id=project_id,
    )
