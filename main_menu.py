import pygame
import os
from button import Button

class Menu:
    """A class to build and draw the menu menu displayed when the game starts."""
    
    def __init__(self, ai_game):
        """Initialize the main menu and it's buttons"""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #Create the buttons
        self.button_play = Button(ai_game, "Play")
        self.button_quit = Button(ai_game, "Quit")
        self.button_fullscreen = Button(ai_game, "Fullscreen")
        self.mute_button = Button(ai_game, "Mute")

        # Position the buttons neatly
        self._position_menu_buttons()


    def _position_menu_buttons(self):
        """Position buttons vertically centered on the main screen"""
        spacing = 80

        self.button_play.rect.center = (
            self.screen_rect.centerx, 
            self.screen_rect.centery - spacing
            )
        self.button_play._prep_msg("Play")

        self.button_fullscreen.rect.center = (
            self.screen_rect.centerx, 
            self.screen_rect.centery
            )
        self.button_fullscreen._prep_msg("Fullscreen")

        self.mute_button.rect.center = (
            self.screen_rect.centerx,
            self.screen_rect.centery + spacing
        )
        self.mute_button._prep_msg("Mute")

        self.button_quit.rect.center = (
            self.screen_rect.centerx, 
            self.screen_rect.centery + 2*spacing
            )
        self.button_quit._prep_msg("Quit Game")

    def draw_menu(self):
        """Draw the main menu screen"""

        #Background colour
        self.screen.fill((25, 25, 60)) # Dark blue background

        #font file path
        font_path = os.path.join("fonts", "Orbitron-Regular.ttf")
        title_font = pygame.font.Font(font_path, 90)

        # Title Text
        title_text = title_font.render("ALIEN INVASION", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen_rect.centerx, 200))
        self.screen.blit(title_text, title_rect)

        # Draw Buttons
        self.button_play.draw_button()
        self.button_fullscreen.draw_button()
        self.mute_button.draw_button()
        self.button_quit.draw_button()

    def check_button_click(self, mouse_pos):
        """Check if any button in the menu is clicked"""

        if self.button_play.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self.ai_game._start_game()

        elif self.button_fullscreen.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self.ai_game.make_fullscreen()
        
        elif self.mute_button.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self.ai_game.toggle_mute()

        elif self.button_quit.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            pygame.quit()
            raise SystemExit

