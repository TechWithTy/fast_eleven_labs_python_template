from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

def unshare_workspace_resource(resource_id: str, resource_type: str) -> dict:
    """
    Unshares a workspace resource with a user.

    Args:
        resource_id (str): The ID of the resource to unshare.
        resource_type (str): The type of the resource to unshare.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.unshare_workspace_resource(
        resource_id=resource_id,
        resource_type=resource_type,
    )
    
