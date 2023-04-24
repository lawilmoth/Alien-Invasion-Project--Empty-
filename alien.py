import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Initialize the alien and set its starting position"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each aien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.settings = ai_game.settings

    def check_edges(self):
        """Returns true if any alien touches the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
