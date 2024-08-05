import pygame

pygame.mixer.init()
torcida = pygame.mixer.music.load('audio/sons_de_torcida.wav')
pygame.mixer.music.play(-1)
kick_sound = pygame.mixer.Sound('audio/ball_kick.wav')
whistle_sound = pygame.mixer.Sound('audio/whistle.wav')
