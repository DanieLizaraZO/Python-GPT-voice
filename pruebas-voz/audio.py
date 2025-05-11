import pygame

# Inicializar el módulo de sonido
pygame.mixer.init()

# Cargar sonidos .wav
sonido1 = pygame.mixer.Sound("./pruebas-python/audio/audio1.wav")
sonido2 = pygame.mixer.Sound("./pruebas-python/audio/audio2.wav")

# Reproducir
sonido1.play()
# Esperar a que termine
while pygame.mixer.get_busy():
    continue

sonido2.play()
while pygame.mixer.get_busy():
    continue
