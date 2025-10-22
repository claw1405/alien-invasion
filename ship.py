import pygame

class Ship():
    """A class to manage the users spaceship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ships image and set its rect
        self.image = pygame.image.load('images/ship.png').convert_alpha()

        #Resize the image: width=60, height=48 (example values)
        self.image = pygame.transform.scale(self.image, (75, 60))

        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 15  # move the ship 15 pixels up

        #store a float for the ships exact horizontal position
        self.x = float(self.rect.x)

        #movement flag. start with a ship that isn't moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        screen_rect = self.screen.get_rect() #updated every frame

        if self.moving_right and self.rect.right < screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Clamp the ship within screen boundaries
        if self.x < 0:
            self.x = 0
        elif self.x + self.rect.width > self.screen_rect.width:
            self.x = self.screen_rect.width - self.rect.width

        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)