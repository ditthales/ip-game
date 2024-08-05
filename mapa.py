import pygame
from bloco import Bloco

mundo = []
rows, cols = 10,10

for x in range(rows):
    col = []
    for y in range(cols):
        col.append('L')

    mundo.append(col)

class Mapa:
    def __init__(self):
        self.tela = pygame.display.get_surface()

        self.sprites_visiveis = pygame.sprite.Group()
        self.obstaculos = pygame.sprite.Group()
        self.rect_colidiveis = []
        self.offset = pygame.math.Vector2()

    def criar_mapa(self, mundo):
        print(mundo)
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

    def desenhar(self):
        self.tela.fill((0, 0, 0)) 
        for sprite in self.sprites_visiveis:
            nova_pos = sprite.rect.topleft
            self.tela.blit(sprite.image, nova_pos)
        for sprite in self.obstaculos:
            nova_pos = sprite.rect.topleft
            self.tela.blit(sprite.image, nova_pos)
        