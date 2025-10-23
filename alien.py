import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""

        super().__init__()
        self.screen = ai_game

        #load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/alien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 50))  # Example size
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.settings = ai_game.settings

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x