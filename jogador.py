import pygame
from constantes import direcoes_movimento, LARGURA_TELA, ALTURA_TELA

class Jogador:
    def __init__(self):
        self.rect = pygame.Rect(450, 450, 50, 30)
        self.velocidade = 2

        self.imagem_direita = pygame.image.load('./playerassets/jogador_direita.png')
        self.imagem_direita = pygame.transform.scale(self.imagem_direita, (30, 48))
        self.imagem_esquerda = pygame.image.load('./playerassets/jogador_esquerda.png')
        self.imagem_esquerda = pygame.transform.scale(self.imagem_esquerda, (30, 48))
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
        elif self.rect.x > LARGURA_TELA - 30:
            self.rect.x = LARGURA_TELA - 30
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > ALTURA_TELA - 48:
            self.rect.y = ALTURA_TELA - 48

    # def desenhar(self, tela):
    #     pygame.draw.rect(tela, 'blue', self.rect)

    def desenhar(self, tela):
        tela.blit(self.imagem_atual, (self.rect.x, self.rect.y))