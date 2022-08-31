import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('../venv/malva.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

