import pygame
import sys
import random

pygame.init()
relogio = pygame.time.Clock()
icone = pygame.image.load("assets/pato.png")
pygame.display.set_icon(icone)
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("FlapPato")

img_pato = pygame.image.load("assets/pato.png").convert_alpha()
img_pato = pygame.transform.smoothscale(img_pato, (45.6, 52.5))
img_pato_voando = pygame.image.load("assets/pato-voando.png").convert_alpha()
img_pato_voando = pygame.transform.smoothscale(img_pato_voando, (45.6, 52.5))
bg = pygame.image.load("assets/background.jpeg").convert()
gameover = gameover = pygame.image.load("assets/gamer-over.png").convert_alpha()
cano_img = pygame.image.load("assets/cano.png").convert_alpha()
cano_img = pygame.transform.smoothscale(cano_img, (50, 450))
cano_cima_img = pygame.transform.flip(cano_img, False, True)

fonte = pygame.font.SysFont("arial", 18)
vel_y = 0
gravidade = 0.5
impulso = -8

x = 200
y = 300

player_rect = pygame.Rect(x, y, 46, 52)

ESPACO = 150
cano_x = 800
cano_x_2 = 1200
gap_y_1 = random.randint(100, 450)
gap_y_2 = random.randint(100, 450)
cano1_cima = pygame.Rect(cano_x, 0, 50, gap_y_1)
cano1_baixo = pygame.Rect(cano_x, gap_y_1 + ESPACO, 50, 600)

cano2_cima = pygame.Rect(cano_x_2, 0, 50, gap_y_2)
cano2_baixo = pygame.Rect(cano_x_2, gap_y_2 + ESPACO, 50, 600)
texto = fonte.render("Desenvolvido por Eike & Miguel • Versão Beta 1.0", True, (255, 255, 255))
sombra = fonte.render("Desenvolvido por Eike & Miguel • Versão Beta 1.0", True, (0, 0, 0))

game_over = False
jogo_ativo = False

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if game_over:
                    game_over = False
                    jogo_ativo = True
                    y = 300
                    vel_y = 0
                    cano_x = 800
                    cano_x_2 = 1200
                elif not jogo_ativo:
                    jogo_ativo = True
                else:
                    vel_y = impulso

    if jogo_ativo:
        cano_x -= 4
        cano_x_2 -= 4
        
        if cano_x < -50:
            cano_x = 800
            gap_y_1 = random.randint(100, 450)

        
        # Segundo cano - AQUI ESTAVA O ERRO
        if cano_x_2 < -50:
            cano_x_2 = 800
            gap_y_2 = random.randint(100, 450)

    player_rect.topleft = (x, y)

    if player_rect.colliderect(cano1_cima) or player_rect.colliderect(cano1_baixo) or player_rect.colliderect(cano2_cima) or player_rect.colliderect(cano2_baixo):
        game_over = True
        jogo_ativo = False


    if jogo_ativo:
        vel_y += gravidade
        y += vel_y

        if y > 600:
            print("game over")
            jogo_ativo = False
            game_over = True

        if y < 0:
            y = 0
            vel_y = 0

    tela.blit(bg, (0,0))

    tela.blit(bg, (0,0))

    if game_over:
        rect = gameover.get_rect(center=(400, 300))
        tela.blit(gameover, rect)
    else:
        if vel_y < -1:
            tela.blit(img_pato_voando, (x, y))
        else:
            tela.blit(img_pato, (x, y))

    tela.blit(cano_cima_img, (cano_x, gap_y_1 - cano_cima_img.get_height()))
    tela.blit(cano_img, (cano_x, gap_y_1 + ESPACO))

    tela.blit(cano_cima_img, (cano_x_2, gap_y_2 - cano_cima_img.get_height()))
    tela.blit(cano_img, (cano_x_2, gap_y_2 + ESPACO))

    cano1_cima = pygame.Rect(cano_x, 0, 50, gap_y_1)
    cano1_baixo = pygame.Rect(cano_x, gap_y_1 + ESPACO, 50, 600)

    cano2_cima = pygame.Rect(cano_x_2, 0, 50, gap_y_2)
    cano2_baixo = pygame.Rect(cano_x_2, gap_y_2 + ESPACO, 50, 600)
    tela.blit(sombra, (11, 571))
    tela.blit(texto, (10, 570))

    pygame.display.update()
    relogio.tick(60)