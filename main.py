import pygame
import math
from constantes import *
from utils import *
from jogador import Jogador
from adversario import Adversario
from bola import Bola
from gol import Gol
from coletavel import Coletavel
from audio import torcida, kick_sound

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
    bolas_restantes = 2
    convites_aceitos = 0

    fonte_pequena = pygame.font.SysFont('arial', 16)
    fonte_grande = pygame.font.SysFont('arial', 32)

    adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 3)]
    bolas_a_coletar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'bola') for _ in range(1)]
    convites_a_aceitar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'convite') for _ in range(2)]

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        if nivel <= MAX_NIVEIS:
            tela.blit(imagem_fundo, (0, 0))

            texto_vidas = fonte_pequena.render(f'Vidas restantes: {vidas}', True, 'white')
            texto_bolas = fonte_pequena.render(f'Bolas restantes: {bolas_restantes}', True, 'white')
            texto_nivel = fonte_pequena.render(f'Nível: {nivel}', True, 'white')
            texto_convites = fonte_pequena.render(f'Convites aceitos: {convites_aceitos}', True, 'white')

            tela.blit(texto_vidas, (33, 10))
            tela.blit(texto_bolas, (33,70))
            tela.blit(texto_nivel, (33, 40))
            tela.blit(texto_convites, (33, 100))

            teclas = pygame.key.get_pressed()
            jogador.mover(teclas)

            if pygame.mouse.get_pressed()[0] and len(bolas) == 0 and bolas_restantes > 0:
                
                mouse_pos = pygame.mouse.get_pos()

                bolas.append(Bola(jogador.rect.x, jogador.rect.y, mouse_pos))

                bolas_restantes -= 1

                kick_sound.play()
            
            for adversario in adversarios:
                adversario.atualizar()
                adversario.desenhar(tela)
            
            for bola_a_coletar in bolas_a_coletar[:]:
                bola_a_coletar.desenhar(tela)

            for convite_a_aceitar in convites_a_aceitar[:]:
                convite_a_aceitar.desenhar(tela)

            gol.desenhar(tela)

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

                        adversarios = [Adversario(gerar_pontos_movimento(), circular=(i % 2 == 1)) for i in range(nivel + 3)]
                        bolas_a_coletar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'bola') for _ in range(2)]
                        convites_a_aceitar = [Coletavel(gerar_random_x(), gerar_random_y(), 10, 10, 'convite') for _ in range(2)]
                        bolas = []
                        vidas = 3
                        gol_marcado = False
                        gol = Gol()

                        if nivel > MAX_NIVEIS:
                            print("Você venceu todos os níveis! Fim de jogo.")
                            tela.fill((0, 255, 0))
                            tela.blit(imagem_fundo, (0, 0))

                            rendered_lines = render_multiline_text(gerar_frase_final(convites_aceitos), fonte_grande, 'white')

                            total_height = len(rendered_lines) * fonte_grande.get_linesize()
                            y_offset = (ALTURA_TELA - total_height) // 2
                            
                            for rendered_line in rendered_lines:
                                line_rect = rendered_line.get_rect(center=(LARGURA_TELA // 2, y_offset))
                                tela.blit(rendered_line, line_rect.topleft)
                                y_offset += fonte_grande.get_linesize()

                            

                        jogador = Jogador()

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

            jogador.desenhar(tela)

        # pygame.display.flip()
        pygame.display.update()
        relogio.tick(FPS)

        

if __name__ == '__main__':
    main()
