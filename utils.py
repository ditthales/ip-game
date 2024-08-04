import random

def gerar_pontos_movimento():
    pontos = []
    for _ in range(random.randint(4, 8)):
        pontos.append((random.randint(100, 900), random.randint(100, 600)))
    return pontos