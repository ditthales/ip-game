import pygame
import random

class Gol:
    def __init__(self):
        self.rect = pygame.Rect(384, 8, 160, 72)

    def desenhar(self, tela):
        pygame.draw.rect(tela, 'gray', self.rect, 1)