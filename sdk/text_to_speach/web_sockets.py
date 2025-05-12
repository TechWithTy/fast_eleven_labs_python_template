from client import get_client

def text_to_speech_stream( voice_id, text, model_id="eleven_monolingual_v1"):
    client = get_client()

    audio_stream = client.generate(
        text=text, voice=voice_id, model=model_id, stream=True
    )

    for chunk in audio_stream:
        yield chunk
