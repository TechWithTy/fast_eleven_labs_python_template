from client import get_client

def get_resource(resource_id: str, resource_type: str) -> dict:
    """
    Gets a resource from the workspace.

    Args:
        resource_id (str): The ID of the resource.
        resource_type (str): The type of the resource.

    Returns:
        dict: The response from the API.
    """
    client = get_client()
    return client.workspace.get_resource(
        resource_id=resource_id,
        resource_type=resource_type,
    )
