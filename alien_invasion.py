import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion :
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #Initialize all pygame modules

        #initialise the clock method
        self.clock = pygame.time.Clock()

        self.settings = Settings() #Call settings module

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True :
            self._check_events() #Check for new events
            self._update_screen() #update screen with bg colour
            self.ship.update()

            #Determine the frame rate for the game in this case 60 the loop will
            #ideally run 60 times per second.
            self.clock.tick(60)

    def _check_events(self):
         #watch for KB and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                          #move the ship to the right
                          self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False

    def _update_screen(self):
          # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_colour)
            self.ship.blitme()
                
            #make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
