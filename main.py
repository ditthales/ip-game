import pygame
from constantes import *
from utils import *
from jogador import Jogador
from adversario import Adversario
from bola import Bola
from gol import Gol

# Inicializa o pygame
pygame.init()

def main():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Jogo de Futebol')

    fundo = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    fundo = fundo.convert()
    fundo.fill('green')
    scroll_fundo = ALTURA_TELA * 1.5

    relogio = pygame.time.Clock()

    nivel = 1
    max_niveis = 10
    jogador = Jogador()
    gol = Gol()
    bolas = []
    gol_marcado = False

    adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 1)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        tela.blit(fundo, (0, 0))
        scroll_fundo -= VELOCIDADE
        if scroll_fundo <= -ALTURA_TELA:
            scroll_fundo = ALTURA_TELA * 1.5

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if teclas[pygame.K_SPACE] and len(bolas) == 0:
            bolas.append(Bola(jogador.rect.x, jogador.rect.y))

        for adversario in adversarios:
            adversario.atualizar()
            adversario.desenhar(tela)

        for bola in bolas[:]:
            bola.atualizar()
            bola.desenhar(tela)
            if bola.rect.y < 0 and not gol_marcado:
                bolas.remove(bola)
                pygame.quit()
                quit()
            else:
                for adversario in adversarios[:]:
                    if bola.rect.colliderect(adversario.rect):
                        bolas.remove(bola)
                        pygame.quit()
                        quit()
                if bola.rect.colliderect(gol.rect):
                    gol_marcado = True
                    print(f"Gol! Nível {nivel} completado.")
                    nivel += 1
                    if nivel > max_niveis:
                        print("Você venceu todos os níveis! Fim de jogo.")
                        pygame.quit()
                        quit()
                    adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 1)]
                    bolas = []
                    gol_marcado = False
                    jogador.rect.topleft = (450, 630)
                    gol.rect.topleft = (400, 0)

        for adversario in adversarios:
            if jogador.rect.colliderect(adversario.rect):
                print("Você foi atingido! Fim de jogo.")
                pygame.quit()
                quit()

        jogador.desenhar(tela)
        gol.desenhar(tela)

        pygame.display.flip()
        relogio.tick(FPS)

        pygame.display.update()

if __name__ == '__main__':
    main()
