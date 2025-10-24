import pygame, os
from button import Button

class GameOverScreen:
    """Display a Game Over screen when a player loses"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        #Buttons
        self.button_play_again = Button(ai_game, "Play Again")
        self.button_main_menu = Button(ai_game, "Main Menu")
        self.button_quit = Button(ai_game, "Quit Game")

        self.sound_played = False

        self._position_buttons()

    def _position_buttons(self):
        """Position the buttons vertically on the screen"""
        spacing = 90

        #Place buttons below score text
        base_y = self.screen_rect.centery + 100

        self.button_play_again.rect.center = (
            self.screen_rect.centerx,
            base_y
        )
        self.button_play_again._prep_msg("Play Again")

        self.button_main_menu.rect.center = (
            self.screen_rect.centerx,
            base_y + spacing
        )
        self.button_main_menu._prep_msg("Main Menu")

        self.button_quit.rect.center = (
            self.screen_rect.centerx,
            base_y + 2 * spacing
        )
        self.button_quit._prep_msg("Quit Game")

    def draw_game_over(self):
        """Draw the game over screen"""
        self.screen.fill((20, 20, 40))

        if not self.sound_played:
            if not self.ai_game.is_muted:
                self.ai_game.game_over_sound.play()
            self.sound_played = True

        #Font setup
        font_path = os.path.join("fonts", "Orbitron-Regular.ttf")
        title_text = pygame.font.Font(font_path, 100)
        text_font = pygame.font.Font(font_path, 40)

        # Game over text
        title_text = text_font.render("GAME OVER", True, (255, 0, 0))
        title_Rect = title_text.get_rect(center=(self.screen_rect.centerx, 200))
        self.screen.blit(title_text, title_Rect)

        #Show final score
        score_text = text_font.render(
            f"Final Score: {self.ai_game.stats.score}", 
            True,
            (255, 255, 255)
        )
        score_rect = score_text.get_rect(center=(self.screen_rect.centerx, 300))
        self.screen.blit(score_text, score_rect)

        # Draw buttons
        self.button_play_again.draw_button()
        self.button_main_menu.draw_button()
        self.button_quit.draw_button()

    def check_button_click(self, mouse_pos):
        """Handle button clicks on the game over screen."""
        if self.button_play_again.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self._stop_sound()
            self.ai_game._start_game()
        
        elif self.button_main_menu.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self._stop_sound()
            self.ai_game.in_menu = True

        elif self.button_quit.rect.collidepoint(mouse_pos):
            if not self.ai_game.is_muted:
                self.ai_game.button_click.play()
            self._stop_sound()
            pygame.quit()
            raise SystemExit
        
    def _stop_sound(self):
        """Stop the game over sound and reset the played flag."""
        self.ai_game.game_over_sound.stop()
        self.sound_played = False


