class Settings:
    """A class to store settings for our game"""

    def __init__(self):
        """Initialize the game's static settings settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.alien_bullet_color = (255, 50, 0)
        self.bullets_allowed = 5
        self.fleet_drop_speed = 10
        self.ship_limit = 2
        self.speedup_scale = 1.1  # 10% speedup
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 5.0

        self.alien_speed = 1.0
        self.powerup_frequency = 30
        self.alien_bullet_speed = self.bullet_speed / 15
        self.fire_frequency = 50000
        # fleet direction of 1 is right
        # -1 is left
        self.fleet_direction = 1

        # Scoreing
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
