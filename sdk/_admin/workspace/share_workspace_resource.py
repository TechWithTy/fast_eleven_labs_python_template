from elevenlabs import ElevenLabs

from client import get_client

def share_workspace_resource(resource_id: str, role: str, resource_type: str) -> dict:
    """
    Shares a workspace resource with a user.

    Args:
        resource_id (str): The ID of the resource to share.
        role (str): The role of the user to share the resource with.
        resource_type (str): The type of the resource to share.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.share_workspace_resource(
        resource_id=resource_id,
        role=role,
        resource_type=resource_type,
    )
