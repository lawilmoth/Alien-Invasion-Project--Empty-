import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Initialize the alien and set its starting position'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each aien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)