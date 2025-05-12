from client import get_client

client = get_client()

client.voices.get_shared(
    page_size=1,
    gender="female",
    language="en",
)
