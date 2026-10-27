from alien import Alien

class FastAlien(Alien):

    def update(self) -> None:
        """Move o alienígena para a direita ou para a esquerda."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x