import pygame
import random
from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = ai_game.screen
        self.speed = 1
        self.radius = 5
        self.type = random.choice(["big_shot"])
        self.color = (0, 0, 200)
        self.rect = pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2,
        )

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)
