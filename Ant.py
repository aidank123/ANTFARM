# Define a ant object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'ant'
import pygame
import random
import Pheremone_Map as pm

# Define constants for the screen width and height
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

p = pm.Pheremone_Map()

class Ant(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Ant, self).__init__()
        self.surf = pygame.Surface((4, 4))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    #add location to pheremone map
    def add_location(self):
        p.add_location([self.rect.x, self.rect.y])
        
    # Keep player on the screen
    def stay_on_screen(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    # Move the sprite based on user keypresses
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        self.stay_on_screen()
            

    def random_pathing(self):
        rand = random.randint(0,3)
        if rand == 0:
            self.rect.move_ip(0, -3)
        if rand == 1:
            self.rect.move_ip(0, 3)
        if rand == 2:
            self.rect.move_ip(-3, 0)
        if rand == 3:
            self.rect.move_ip(3, 0)
        
    
        self.stay_on_screen()