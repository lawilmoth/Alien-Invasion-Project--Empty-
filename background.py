import pygame
import random


class Background:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bg_color = self.settings.bg_color

        self.stars = []

        for i in range(500):
            star = Star(ai_game)
            self.stars.append(star)

    def draw_background(self):
        self.screen.fill(self.bg_color)

        for star in self.stars:
            if star.can_move:
                star.update()
            star.draw()


class Star:
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (255, 255, 255)
        self.x = random.randint(0, self.settings.screen_width)
        self.y = random.randint(0, self.settings.screen_height)
        self.r = random.choice([1, 1, 1, 1, 1, 2, 2, 3])
        self.can_move = random.choice([True, False, False, False, False, False])
        self.speed = random.choice(
            [0.1, 0.05, 0.05, 0.05, 0.02, 0.02, 0.02, 0.02, 0.005, 0.005, 0.005]
        )

    def update(self):

        self.y += self.speed
        if self.y >= self.settings.screen_height:
            self.y = 0
        # update the bullet position
        # self.cirle.y = self.y

    def draw(self):
        """Draw the bullet to the screen"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
