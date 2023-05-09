class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initalizes the statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.new_high_score = False
        with open("high_score.txt", "r") as high_score:

            self.high_score = int(high_score.readline())
            self.top_player = high_score.readline()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
