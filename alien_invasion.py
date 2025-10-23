import sys, pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
class AlienInvasion :
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init() #Initialize all pygame modules

        #initialise the clock method
        self.clock = pygame.time.Clock()

        self.settings = Settings() #Call settings module

        self.windowed_mode()

        # Create an instance to store in game statistics
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Make an alien and then keep adding aliens until we run out of space
        # Spacing between aliens is equal to one alien width and one alien 
        # height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            #finish a row; reset x value, and increment the y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
           new_alien = Alien(self)
           new_alien.x = x_position
           new_alien.rect.x = x_position
           new_alien.rect.y = y_position
           self.aliens.add(new_alien)

    def _ship_hit(self):
        """Respond to the ship being hit by alien"""
        # Decrement ships_left
        self.stats.ships_left -= 1

        # Get rid of any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(0.5) 

    def make_fullscreen(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
    
    def windowed_mode(self):
         self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """Start the main loop for the game"""
        while True :
            self._check_events() #Check for new events
            self._update_screen() #update screen with bg colour
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

            #Determine the frame rate for the game in this case 60 the loop will
            #ideally run 60 times per second.
            self.clock.tick(60)

    def _check_events(self):
         #watch for KB and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)         

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_f:
             self.make_fullscreen()
        elif event.key == pygame.K_ESCAPE:
             self.windowed_mode()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()
        
        #Get rid of bullets that have disappeared off screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet alien collisions"""
        #Check for any bullets that have hit aliens.
        #If so get rid of the bullets and the alien
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            #Destroy existing bullets and repopulate the fleet
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self):
         """Check if any aliens have reached the bottom of the screen"""
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   #Treat this the same if the ship got hit
                   self._ship_hit()
                   break


    def _update_aliens(self):
        """Update the position of all aliens in the fleet"""
        #Check if the fleet is at the edge, then update positions
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()

        # Look for any aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
         """Respond appropriately if the alien have reached an edge"""
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break
              
    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
          # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_colour)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.ship.blitme()
            self.aliens.draw(self.screen) 

            #make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
