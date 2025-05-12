from client import get_client
def list_project_snapshots(project_id: str) -> list[dict]:
    
    client = get_client()

    client.studio.projects.get_snapshots(
        project_id="21m00Tcm4TlvDq8ikWAM",
    )
