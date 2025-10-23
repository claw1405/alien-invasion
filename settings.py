class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (25, 25, 112)  # Midnight blue background

        # Ship settings
        self.ship_limit = 3  # Number of lives/ships the player gets

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 0, 0)  # Red bullets
        self.bullets_allowed = 6  # Max bullets on screen at once

        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien points value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # Scoring settings
        self.alien_points = 50

        # fleet_direction of 1 means right; -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)