import pygame
from bloco import Bloco

mundo = [[]]

for x in range(10):
  for y in range(10):
    mundo[x][y] = 'G'

class Mapa:
    def __init__(self):
        self.tela = pygame.display.get_surface()

        self.sprites_visiveis = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.rect_colidiveis = []
        self.offset = pygame.math.Vector2()

    def criar_mapa(self, mundo):
        for t_linha in enumerate(mundo):
            l_index = t_linha[0]
            for t_bloco in enumerate(t_linha[1]):
                c_index = t_bloco[0]
                x = c_index * 8
                y = l_index * 8
                if t_bloco[1] == 'G':
                    Bloco(x, y, [self.obstaculos], 'grama')
                    surface_block = pygame.Surface((8,8))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'L':
                    Bloco(x, y, [self.obstaculos], 'linha')
                    surface_block = pygame.Surface((8,8))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
                elif t_bloco[1] == 'LG':
                    Bloco(x, y, [self.obstaculos], 'linha_do_gol')
                    surface_block = pygame.Surface((8,8))
                    rect_surface = surface_block.get_rect(topleft = (x,y))
                    self.rect_colidiveis.append(rect_surface)
    def desenhar(self, off_coords):
        self.rect_colidiveis = []
        self.offset.x = off_coords[0]
        self.offset.y = off_coords[1]
        for sprite in self.sprites_visiveis:
            nova_pos = sprite.rect.topleft + self.offset
            self.tela.blit(sprite.image, nova_pos)
        for sprite in self.obstaculos:
            nova_pos = sprite.rect_inicial.topleft + self.offset
            sprite.rect.topleft = nova_pos
            self.rect_colidiveis.append(sprite.rect)
            self.tela.blit(sprite.image, nova_pos)