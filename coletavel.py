import pygame


class Coletavel:
    def __init__(self, x, y, largura, altura, type):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.type = type
        if type == 'bola':
            self.image = './coletaveisassets/ball.png'
            self.color = 'yellow'
        else:
            self.image = './coletaveisassets/heart.png'
            self.color = 'aquamarine'


    def desenhar(self, tela):
        rect = self.rect()
        pygame.draw.rect(tela, self.color, rect)


    def rect(self):
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x, self.y))
        return rectangle_coletavel

    def get_pc(self):
        return self.x, self.y