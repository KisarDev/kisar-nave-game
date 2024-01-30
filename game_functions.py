import sys
import pygame


def check_events():
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Atualiza as imagens na
    tela e alterna para a nova tela."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
