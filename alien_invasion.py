import game_functions as gf
from settings import Settings
from ship import Ship
import pygame
from pygame.sprite import Group


def run_game():

    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # troca a cor da tela em cada frame
    screen.fill(ai_settings.bg_color)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # Inicia o laço principal do jogo
    while True:
        ship.update()

        # Livra-se dos projéteis que desapareceram
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

        gf.update_aliens(ai_settings, aliens)

        # Observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)

        # Deixa a tela mais recente visível
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()
