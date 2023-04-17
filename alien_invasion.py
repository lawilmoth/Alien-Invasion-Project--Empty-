'''
Alien Invasion Project from Python Crash Course
Chapters 12 - 14
Page 227 of the book.agee 265 of the PDF
'''

import sys
import pygame

class AlienInvasion:
    '''Manages the game and create resources'''

    def __init__(self):
        '''Initialized the game'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        '''Control the loop for the game'''
        while True:
            #Look for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()    


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()