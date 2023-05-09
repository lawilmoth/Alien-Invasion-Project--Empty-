import random
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Initialize the alien and set its starting position"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image
        self.image_green = pygame.image.load("images/alien.png").convert_alpha()
        self.image_red = pygame.image.load("images/alien_red.png")
        self.image = self.image_green
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        # Start each aien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.mad_multiplier = 1

        self.settings = ai_game.settings
        self.is_mad = False
        r = random.randint(0, self.settings.powerup_frequency)
        if r == 0:
            self.has_powerup = True
        else:
            self.has_powerup = False

    def check_edges(self):
        """Returns true if any alien touches the edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right or left"""
        self.x += (
            self.settings.alien_speed
            * self.settings.fleet_direction
            * self.mad_multiplier
        )
        self.rect.x = self.x

    def change_color(self):
        if self.image == self.image_green:
            self.image = self.image_red
        else:
            self.image = self.image_green

    def get_mad(self):
        self.mad_multiplier *= 3
        self.is_mad = True

    def roll_to_shoot(self):
        if not self.is_mad:
            r = random.randint(0, self.settings.fire_frequency)
        else:
            r = random.randint(0, 250)
        if r == 0:
            return True
