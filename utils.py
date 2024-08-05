import random

def gerar_pontos_movimento():
    pontos = []
    for _ in range(random.randint(4, 8)):
        pontos.append((random.randint(100, 900), random.randint(100, 600)))
    return pontos

def gerar_random_x():
    return random.randint(10, 1200)

def gerar_random_y():
    return random.randint(10, 750)

def gerar_drop():
    num_drop = random.randint(1, 3)

    if num_drop == 1:
        return 'bola'
    else:
        return 'convite'