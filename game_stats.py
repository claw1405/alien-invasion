class GameStats :
    """Track statistics for alien invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Store the current high score
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change throughout the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
