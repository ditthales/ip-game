import pygame
from constantes import *

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(450, 450, LARGURA_JOGADOR, ALTURA_JOGADOR)
        self.velocidade = 2

        self.imagem_direita = pygame.image.load('./playerassets/jogador_direita.png')
        self.imagem_direita = pygame.transform.scale(self.imagem_direita, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem_esquerda = pygame.image.load('./playerassets/jogador_esquerda.png')
        self.imagem_esquerda = pygame.transform.scale(self.imagem_esquerda, (LARGURA_JOGADOR, ALTURA_JOGADOR))
        self.imagem_atual = self.imagem_direita

    def mover(self, teclas):
        deslocamento = (0, 0)
        for tecla in direcoes_movimento:
            if teclas[tecla]:
                deslocamento = (deslocamento[0] + direcoes_movimento[tecla][0], deslocamento[1] + direcoes_movimento[tecla][1])
        
        self.rect.x += deslocamento[0] * self.velocidade
        self.rect.y += deslocamento[1] * self.velocidade

        if deslocamento[0] > 0:
            self.imagem_atual = self.imagem_direita
        elif deslocamento[0] < 0:
            self.imagem_atual = self.imagem_esquerda
        
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > LARGURA_TELA - LARGURA_JOGADOR:
            self.rect.x = LARGURA_TELA - LARGURA_JOGADOR
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > ALTURA_TELA - ALTURA_JOGADOR:
            self.rect.y = ALTURA_TELA - ALTURA_JOGADOR

    # def desenhar(self, tela):
    #     pygame.draw.rect(tela, 'blue', self.rect)

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, (self.rect.x, self.rect.y))