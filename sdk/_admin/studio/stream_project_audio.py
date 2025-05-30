from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def stream_project_audio(project_id: str, project_snapshot_id: str) -> dict:
    """
    Stream audio for a specific project snapshot.

    Args:
        project_id: The ID of the project.
        project_snapshot_id: The ID of the project snapshot.

    Returns:
        A dictionary containing the streaming details.
    """
    client = get_client()
    
    return client.studio.projects.stream_audio(
        project_id=project_id,
        project_snapshot_id=project_snapshot_id,
    )
