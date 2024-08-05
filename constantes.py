import pygame

# Define as direções de movimento
direcoes_movimento = {
    pygame.K_w: (0, -2),
    pygame.K_s: (0, 2),
    pygame.K_a: (-2, 0),
    pygame.K_d: (2, 0),
    pygame.K_UP: (0, -2),
    pygame.K_DOWN: (0, 2),
    pygame.K_LEFT: (-2, 0),
    pygame.K_RIGHT: (2, 0)
}

LARGURA_TELA, ALTURA_TELA = 928, 576

FPS = 100

VELOCIDADE = 1.5

MAX_NIVEIS = 10

ALTURA_JOGADOR = 48
LARGURA_JOGADOR = 30

CONVITES = [
    'jantar com a rainha da Dinamarca',
    'pelada com o Dalai Lama',
    'jogo de xadrez com o Papa',
    'passeio de foguete com o Elon Musk',
    'aula de teórica com Ruy',
    'ser monitor de IP no CIn',
    'ser garoto propaganda de Marcelinho',
    'disputar a OPEI',
    
]