import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A Class that manages bullets fired from the ship'''

    def __init__(self, ai_game):
        '''Create bullets at the ships current location'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and set the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets position as a decimal value.
        self.y = float(self.rect.y)
    def update(self):
        '''Move the bullets up the screen'''
        #update the decimal position of the bullets
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draw the bullet on the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)