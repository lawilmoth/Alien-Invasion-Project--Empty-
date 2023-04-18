'''
Alien Invasion Project from Python Crash Course
Chapters 12 - 14
Page 227 of the book. Page 265 of the PDF
'''

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Manages the game and create resources'''

    def __init__(self):
        '''Initialized the game'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))   
        self.ship = Ship(self)
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        '''Control the loop for the game'''
        while True:
            #Look for keyboard and mouse events
            self._check_events()
            self._update_screen()
        
    def _check_events(self): 
        '''Check events in the game'''   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        '''Updates images and flips the screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  
        #displays the screen
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()