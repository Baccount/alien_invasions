import pygame

class Ship:
    '''A class to manage the ship'''
    def __init__(self, ai_game):
        '''Initialize the ship and set its starting position.'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Store the decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the ships movement based on the movement flag'''
        #update the ships x value not the rect value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)