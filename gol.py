import pygame
import random

class Gol:
    def __init__(self):
        self.rect = pygame.Rect(400, 0, 200, 50)

    def desenhar(self, tela):
        pygame.draw.rect(tela, 'grey', self.rect, 2)
