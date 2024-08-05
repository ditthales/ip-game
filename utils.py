import random
from constantes import LARGURA_TELA, ALTURA_TELA, CONVITES
import pygame

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
    
def gerar_roles(n):

     return random.sample(CONVITES, n)

def gerar_frase_final(n):

    if n == 0:

        frase_base = 'Você finalizou todos os níveis,\nmas não conseguiu aceitar\nnenhum convite para rolê.\nQue pena!'

    else:
        roles_aleatorios = gerar_roles(n)

        frase_base = f'Você finalizou todos os níveis\ne coletou {n} convites.\n\nVocê aceitou:'

        for role in roles_aleatorios:
            frase_base += f'\n- {role}'
    
    return frase_base

def render_multiline_text(text, font, color):
    lines = text.split('\n')
    rendered_lines = []
    for line in lines:
        rendered_lines.append(font.render(line, True, color))
    return rendered_lines


def esperar_pelo_proximo_evento():
    # Espera até que um evento de mouse seja registrado
    evento = None
    while not evento:
        evento = pygame.event.wait()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            break