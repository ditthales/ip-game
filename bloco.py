import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y, group, argumento) -> None:

        super().__init__(group)
        self.argumento = argumento
        self.x = x
        self.y = y

        if argumento == 'grama':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/grama.png'),(8,8))
            
        elif argumento == 'linha':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/linha.png'),(8,8))

        elif argumento == 'linha_do_gol':
            self.image = pygame.transform.scale(pygame.image.load('./tiles/linha.png'),(8,8))

        self.rect = self.image.get_rect(topleft=(x,y))
        self.rect_inicial = self.image.get_rect(topleft=(x,y))