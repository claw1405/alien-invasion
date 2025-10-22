class Settings :
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (25, 25, 112)

        #set the bullets attributes
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 0, 0)

        #set the spaceships speed
        self.ship_speed = 1.5