from elevenlabs import ElevenLabs

client = ElevenLabs(
    api_key="YOUR_API_KEY",
)
client.conversational_ai.get_conversations()
