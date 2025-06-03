from openai import OpenAI # Librería de openAI
from config import api_key # Clave de OpenAI
import pygame # para leer audio
from pathlib import Path
from datetime import date # Fecha del día de hoy
from text_to_speech import textToSpeech # Función para pasar a audio

speech_file_path = Path(__file__).parent / "Audios" /"speech.mp3"

pygame.mixer.init()

# Memoria o contexto de nuestra IA
memoryMessage = [{
    "role":"system",
    "content":f"Eres una IA llamada Sonia que responde No lee sino escucha y responde amablemente dudas con una respuesta precisa y sin extenderse mucho y si te preguntan que fecha es hoy, recuerda que estamos a {date.today()}"
}]

# Llamada a chatGPT
client = OpenAI(api_key=api_key)  # Seguro y recomendado
def serviceAI(response):
    
    memoryMessage.append({"role":"user","content": response})
    
    completion = client.chat.completions.create(
        model="gpt-4.1",
        # model="gpt-3.5-turbo",
        messages=memoryMessage
    )
    
    # Incluye la respuesta de chatGPT
    respuesta = completion.choices[0].message.content
    
    memoryMessage.append({"role": "assistant", "content": respuesta})

    
    if len(memoryMessage) > 16:
        del memoryMessage[1:3]
    
    textToSpeech(respuesta) # Para pasar la respuesta a audio
    sonido1 = pygame.mixer.Sound(speech_file_path)
    # Reproducir
    sonido1.play()
    # Esperar a que termine
    while pygame.mixer.get_busy():
        continue
    
    return respuesta
