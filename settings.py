class Settings:
    """A class to store settings for our game"""

    def __init__(self):
        """Initialize the games settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        self.bullets_allowed = 3

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 is right
        # -1 is left
        self.fleet_direction = 1

        self.ship_limit = 3
