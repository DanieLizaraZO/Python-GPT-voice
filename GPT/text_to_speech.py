from pathlib import Path
from openai import OpenAI
from .config import api_key

client = OpenAI(api_key=api_key)
speech_file_path = Path(__file__).parent / "speech.wav"
def textToSpeech(response):
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="ash",
        input=response,
        instructions="Hablas en Español con un tono amigable"
    ) as response:
        response.stream_to_file(speech_file_path)