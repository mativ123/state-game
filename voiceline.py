import pygame
class Voiceline:
    def __init__(self, path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(path)
        sound.play()



Voiceline("untitled.wav")


pygame.init()
Yellow = (255, 255, 0)

x = 400
y = 400

screen = pygame.display.set_mode((x, y))



while True:
    screen.fill(Yellow)
