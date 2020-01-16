import sys
from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game and create game resources'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bullets = pygame.sprite.Group()
        #Set background color
        self.bg_color = (230, 230, 230)


        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
    def run_game(self):
        '''Starts the main loop for the game.'''
        while True:
            #update ships movement
            self.ship.update()
            #Check for keyboard interactions or mouse interactions
            self._check_events()
            self.update_bullets()
            #redraw the screen
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

                #On key release stop the ship
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''Respond to key events'''
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to left
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            #If you click 'q' the game exits
            sys.exit()

    def _check_keyup_events(self,event):
        '''Respond to key events'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently draw screen visable
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def update_bullets(self):
        # Update the bullets position
        self.bullets.update()
        # Get rid of bullets that have disapperred off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

if __name__ == '__main__':
    #Make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
