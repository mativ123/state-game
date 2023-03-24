# Her importere jeg pygame
import pygame

# Her definere jeg klassen "Voiceline"
class Voiceline:
    def __init__(self, path):
        # Her initialisere jeg pygame mixer
        pygame.mixer.init()

        # Her loader lydden
        sound = pygame.mixer.Sound(path)

        # Her spiller lyden så
        sound.play()
