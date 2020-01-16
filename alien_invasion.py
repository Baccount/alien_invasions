import sys
from settings import Settings
import pygame
from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        #Set background color
        self.bg_color = (230, 230, 230)


        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
    def run_game(self):
        '''Starts the main loop for the game.'''
        while True:
            #Check for keyboard interactions or mouse interactions
            self._check_events()
            #redraw the screen
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently draw screen visable
        pygame.display.flip()

if __name__ == '__main__':
    #Make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
