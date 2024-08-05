import pygame

class Coletavel:
    def __init__(self, x, y, largura, altura, type):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.type = type

        if type == 'bola':
            self.image = pygame.image.load('./playerassets/bola.png')
        else:
            self.image = pygame.image.load('./coletaveisassets/convite.png')

        self.image = pygame.transform.scale(self.image, (18, 18))


    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))

    def rect(self):
        surface_coletavel = pygame.Surface((self.largura, self.altura))
        rectangle_coletavel = surface_coletavel.get_rect(center=(self.x, self.y))
        return rectangle_coletavel

    def get_pc(self):
        return self.x, self.y