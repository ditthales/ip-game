import pygame
import math

class Adversario:
    def __init__(self, pontos_movimento, circular=False):
        self.rect = pygame.Rect(pontos_movimento[0][0], pontos_movimento[0][1], 30, 48)
        self.velocidade = 2  # Velocidade aumentada
        self.pontos_movimento = pontos_movimento
        self.index_ponto = 0
        self.circular = circular
        self.angulo = 0
        self.raio = 100

        self.imagem_direita = pygame.image.load('./playerassets/adversario-direita.png')
        self.imagem_direita = pygame.transform.scale(self.imagem_direita, (30, 48))
        self.imagem_esquerda = pygame.image.load('./playerassets/adversario-esquerda.png')
        self.imagem_esquerda = pygame.transform.scale(self.imagem_esquerda, (30, 48))
        self.imagem_atual = self.imagem_direita

    def atualizar(self):
        if self.circular:
            centro_x, centro_y = self.pontos_movimento[0]
            self.rect.x = centro_x + int(self.raio * math.cos(math.radians(self.angulo)))
            self.rect.y = centro_y + int(self.raio * math.sin(math.radians(self.angulo)))
            self.angulo = (self.angulo + self.velocidade) % 360
        else:
            destino_x, destino_y = self.pontos_movimento[self.index_ponto]
            if self.rect.x < destino_x:
                self.rect.x += self.velocidade
            elif self.rect.x > destino_x:
                self.rect.x -= self.velocidade
            
            if self.rect.y < destino_y:
                self.rect.y += self.velocidade
            elif self.rect.y > destino_y:
                self.rect.y -= self.velocidade

            if abs(self.rect.x - destino_x) < self.velocidade and abs(self.rect.y - destino_y) < self.velocidade:
                self.index_ponto = (self.index_ponto + 1) % len(self.pontos_movimento)

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, (self.rect.x, self.rect.y))