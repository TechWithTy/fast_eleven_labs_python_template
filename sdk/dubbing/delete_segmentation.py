
from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client


def delete_segment(dubbing_id: str, segment_id: str) -> dict:
    """
    Delete a segment from a dubbing resource.

    Args:
        dubbing_id: The ID of the dubbing resource.
        segment_id: The ID of the segment.

    Returns:
        A dictionary containing the deletion details.
    """
    client = get_client()
    
    return client.dubbing.delete_segment(
        dubbing_id=dubbing_id,
        segment_id=segment_id,
    )
