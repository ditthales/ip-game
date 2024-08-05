import pygame
import math
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

    imagem_fundo = pygame.image.load('./campinho.png')
    imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA_TELA, ALTURA_TELA))

    relogio = pygame.time.Clock()

    nivel = 1
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

        tela.blit(imagem_fundo, (0, 0))

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if pygame.mouse.get_pressed()[0] and len(bolas) == 0:
            
            mouse_pos = pygame.mouse.get_pos()

            bolas.append(Bola(jogador.rect.x, jogador.rect.y, mouse_pos))
        
        for adversario in adversarios:
            adversario.atualizar()
            adversario.desenhar(tela)

        for bola in bolas[:]:
            bola.desenhar(tela)
            bola_rect = bola.rect()
            if bola.saiu_tela() and not gol_marcado:
                bolas.remove(bola)
                print("chutou pra fora")
            else:
                for adversario in adversarios[:]:
                    
                    if bola.checar_se_bateu(bola_rect, adversario.rect):
                        bolas.remove(bola)
                        print("atingiu o adversário")
                if bola.checar_se_bateu(bola_rect, gol.rect):
                    gol_marcado = True
                    print(f"Gol! Nível {nivel} completado.")
                    nivel += 1
                    if nivel > MAX_NIVEIS:
                        print("Você venceu todos os níveis! Fim de jogo.")
                        pygame.quit()
                        quit()
                    adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 1)]
                    bolas = []
                    gol_marcado = False
                    jogador = Jogador()
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
