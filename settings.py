class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
Alienígena."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # config aliens:
        self.alien_speed_factor = 0
        self.fleet_drop_speed = 0.5
        self.fleet_direction = 1
