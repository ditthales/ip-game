import pygame

class Bola:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x + 22, y, 6, 20)
        self.velocidade = 15

    def atualizar(self):
        self.rect.y -= self.velocidade

    def desenhar(self, tela):
        pygame.draw.rect(tela, 'white', self.rect)