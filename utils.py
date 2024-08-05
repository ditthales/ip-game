import random
from constantes import LARGURA_TELA, ALTURA_TELA

def gerar_pontos_movimento():
    pontos = []
    for _ in range(random.randint(4, 8)):
        pontos.append((random.randint(0, LARGURA_TELA), random.randint(0, ALTURA_TELA)))
    return pontos

def gerar_random_x():
    return random.randint(10, LARGURA_TELA)

def gerar_random_y():
    return random.randint(10, ALTURA_TELA)

def gerar_drop():
    num_drop = random.randint(1, 3)

    if num_drop == 1:
        return 'bola'
    else:
        return 'convite'