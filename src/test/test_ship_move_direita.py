import pygame
from src.ship import Ship
from src.settings import Settings

def test_ship_move_direita():
    # Inicializa o Pygame
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    
    settings = Settings()
    
    ship = Ship(screen, settings)
    
    x_initial = ship.x
    
    ship.moving_right = True
    ship.update()
    
    assert ship.x > x_initial
    
    