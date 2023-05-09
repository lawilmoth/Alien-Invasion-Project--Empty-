import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object from the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a rect at (0,0) then set the correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        # update the bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienBullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_game, alien):
        """Create a bullet object from the ships current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Create a rect at (0,0) then set the correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = alien.rect.midtop

        # Store the bullet's position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y += self.settings.alien_bullet_speed
        # update the bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
