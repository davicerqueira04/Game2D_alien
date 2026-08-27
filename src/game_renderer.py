class GameRenderer:
    """Classe responsável por renderizar os elementos do jogo na tela."""

    def __init__(self, screen, ship, aliens, bullets, bg_color) -> None:
        self.screen = screen
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.bg_color = bg_color

    def render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
