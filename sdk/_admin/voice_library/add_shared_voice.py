from app.core.third_party_integrations.eleven_labs_home.sdk.client import get_client

client = get_client()

client.voices.add_sharing_voice(
    public_user_id="63e84100a6bf7874ba37a1bab9a31828a379ec94b891b401653b655c5110880f",
    voice_id="sB1b5zUrxQVAFl2PhZFp",
    new_name="Alita",
)
