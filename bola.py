import pygame
import math
from constantes import ALTURA_TELA, LARGURA_TELA

class Bola:
    def __init__(self, x, y, mouse_pos):
        self.x = x
        self.y = y
        self.xm = mouse_pos[0]
        self.ym = mouse_pos[1]
        self.velocidade = 30
        self.angulo = math.atan2(self.y - self.ym, self.x - self.xm)
        self.x_pos = math.cos(self.angulo) * self.velocidade
        self.y_pos = math.sin(self.angulo) * self.velocidade
        self.pos_verdadeira = (self.x, self.y)
        
    def rect(self):
        surface_bullet = pygame.Surface((10,10))
        rectangle_bullet = surface_bullet.get_rect(center = self.truepos)
        return rectangle_bullet

    def checar_se_bateu(self, rect_bola, rect_objeto):
        if rect_bola.colliderect(rect_objeto):
            return True
        else:
            return False

    def desenhar(self, tela):
        self.x -= self.x_pos
        self.y -= self.y_pos
        self.truepos = (self.x, self.y)
        tela.blit(pygame.transform.scale(pygame.image.load('./coletaveisassets/ball.png'),(10,10)), (self.x, self.y))
        
    def saiu_tela(self):
        return self.y < 0 or self.y > ALTURA_TELA or self.x < 0 or self.x > LARGURA_TELA