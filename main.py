import sys
import os
import pygame
from pathlib import Path
import speech_recognition as sr

from GPTPython import serviceAI
pygame.mixer.init()
# Crear un reconocedor
r = sr.Recognizer()

speech_file_path = Path(__file__).parent / "Audios" / "despedida.mp3"

while True:
    # Usar el micrófono como fuente de entrada
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es-ES")
            palabraClave = "gracias"
            print(f"Lo que se te escuchó: {texto}")
            if palabraClave in texto.lower():
                # Cargar y reproducir el archivo correctamente
                pygame.mixer.music.load(str(speech_file_path))
                pygame.mixer.music.play()

                print("Gracias a ti")
                
                # Esperar a que termine el audio antes de salir
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                break
            else:
                # print(f"IA: {serviceAI(texto)}")
                print(f"\nBOT: {serviceAI(texto)}")
            

        except sr.UnknownValueError:
            print("No entendí lo que dijiste")
        except sr.RequestError as e:
            print("Error al conectar con el servicio de reconocimiento de voz:", e)
