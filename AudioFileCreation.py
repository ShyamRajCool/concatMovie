from elevenlabs.client import ElevenLabs
from elevenlabs import save

client = ElevenLabs(
  api_key="API-Key",
)
audio = client.text_to_speech.convert(
    text="",#Enter your text here
    voice_id="", #Choose a Voice_id
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

save(audio,"FilePlaceHolder.mp3") #Save the Audio file using your preferred file name
