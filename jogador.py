import pygame
from constantes import direcoes_movimento

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(450, 630, 50, 30)
        self.velocidade = 4

    def mover(self, teclas):
        deslocamento = (0, 0)
        for tecla in direcoes_movimento:
            if teclas[tecla]:
                deslocamento = (deslocamento[0] + direcoes_movimento[tecla][0], deslocamento[1] + direcoes_movimento[tecla][1])
        
        self.rect.x += deslocamento[0] * self.velocidade
        self.rect.y += deslocamento[1] * self.velocidade
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 950:
            self.rect.x = 950
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 670:
            self.rect.y = 670

    def desenhar(self, tela):
        pygame.draw.rect(tela, 'blue', self.rect)