import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, message):
        """Initialize button attribute"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of a button
        self.width, self.height = 200, 50
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(message)

    def _prep_msg(self, message):
        """Turn text into a rendered image and center text on the button"""
        self.msg_image = self.font.render(message, True, self.text_colour,
                self.button_colour)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw a blank button and then draw message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

        