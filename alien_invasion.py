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
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        pygame.display.set_caption('Alien Invasion')

    def run_game(self): 
        '''Control the loop for the game'''
        while True:
            #Look for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
        
    def _check_events(self):  
        '''Check events in the game'''   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        '''Updates images and flips the screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  
        #displays the screen
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            #Move ship right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            #Move ship right
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()