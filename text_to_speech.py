from pathlib import Path
from openai import OpenAI
from config import api_key

# Este Bloque de Código es el encargado de recibir el texto y transformarlo a Audio
client = OpenAI(api_key=api_key)
speech_file_path = Path(__file__).parent / "Audios" / "speech.mp3"

def textToSpeech(response):
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="nova",
        input=response,
        instructions="Hablas en Español con un tono amigable"
    ) as response:
        response.stream_to_file(speech_file_path)