import pygame

class Ship():
    """A class to manage the users spaceship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ships image and set its rect
        self.image = pygame.image.load('images/ship.png').convert_alpha()

        #Resize the image: width=60, height=48 (example values)
        self.image = pygame.transform.scale(self.image, (75, 60))

        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 15  # move the ship 15 pixels up

        #movement flag. start with a ship that isn't moving
        self.moving_right = False

    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right:
            self.rect.x += 1


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)