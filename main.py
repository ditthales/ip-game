import pygame
import math
from constantes import *
from utils import *
from jogador import Jogador
from adversario import Adversario
from bola import Bola
from gol import Gol
from coletavel import Coletavel

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

    vidas = 3
    bolas_restantes = 3
    convites_aceitos = 0

    adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 1)]
    bolas_a_coletar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'bola') for _ in range(3)]
    convites_a_aceitar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'convite') for _ in range(3)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        tela.blit(imagem_fundo, (0, 0))

        texto_vidas = pygame.font.SysFont('arial', 16).render(f'Vidas restantes: {vidas}', True, 'white')
        texto_bolas = pygame.font.SysFont('arial', 16).render(f'Bolas restantes: {bolas_restantes}', True, 'white')
        texto_nivel = pygame.font.SysFont('arial', 16).render(f'Nível: {nivel}', True, 'white')
        texto_convites = pygame.font.SysFont('arial', 16).render(f'Convites aceitos: {convites_aceitos}', True, 'white')

        tela.blit(texto_vidas, (33, 10))
        tela.blit(texto_bolas, (33,70))
        tela.blit(texto_nivel, (33, 40))
        tela.blit(texto_convites, (33, 100))

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas)

        if pygame.mouse.get_pressed()[0] and len(bolas) == 0:
            
            mouse_pos = pygame.mouse.get_pos()

            bolas.append(Bola(jogador.rect.x, jogador.rect.y, mouse_pos))

            # bolas_restantes -= 1
        
        for adversario in adversarios:
            adversario.atualizar()
            adversario.desenhar(tela)
        
        for bola_a_coletar in bolas_a_coletar[:]:
            bola_a_coletar.desenhar(tela)

        for convite_a_aceitar in convites_a_aceitar[:]:
            convite_a_aceitar.desenhar(tela)

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
                    bolas_a_coletar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'bola') for _ in range(3)]
                    convites_a_aceitar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'convite') for _ in range(3)]
                    bolas = []
                    vidas = 3
                    gol_marcado = False
                    jogador = Jogador()
                    gol.rect.topleft = (400, 0)

        for adversario in adversarios:
            if jogador.rect.colliderect(adversario.rect):
                vidas -= 1
                adversarios.remove(adversario)
                adversarios.append(Adversario(gerar_pontos_movimento(), circular=adversario.circular))

        for bola_a_coletar in bolas_a_coletar:
            if jogador.rect.colliderect(bola_a_coletar.rect()):
                bolas_restantes += 1
                bolas_a_coletar.remove(bola_a_coletar)

        for convite_a_aceitar in convites_a_aceitar:
            if jogador.rect.colliderect(convite_a_aceitar.rect()):
                convites_aceitos += 1
                convites_a_aceitar.remove(convite_a_aceitar)


        if vidas == 0:
            print("Você perdeu todas as vidas! Fim de jogo.")
            pygame.quit()
            quit()

        if bolas_restantes == 0:
            print("Você perdeu todas as bolas! Fim de jogo.")
            pygame.quit()
            quit()

        jogador.desenhar(tela)
        gol.desenhar(tela)

        # pygame.display.flip()
        pygame.display.update()
        relogio.tick(FPS)

        

if __name__ == '__main__':
    main()
