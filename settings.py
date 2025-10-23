class Settings :
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (25, 25, 112)

        #set the bullets attributes
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 0, 0)
        self.bullets_allowed = 6

        #set the spaceships speed
        self.ship_speed = 1.5

        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1