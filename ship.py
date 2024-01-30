import pygame


class Ship():
    def __init__(self, screen):
        """Inicializa a espaçonave e define sua
        posição inicial."""
        self.screen = screen
        # Carrega a imagem da espaçonave e obtém seu rect u self.image =
        self.image = pygame.image.load('midia/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela x
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)
