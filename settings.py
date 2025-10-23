class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (25, 25, 112)  # Midnight blue background

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3  # Number of lives/ships the player gets

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 0, 0)  # Red bullets
        self.bullets_allowed = 6  # Max bullets on screen at once

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 means right; -1 means left
        self.fleet_direction = 1