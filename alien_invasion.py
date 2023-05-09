"""
Alien Invasion Project from Python Crash Course
Chapters 12 - 14
Page 227 of the book. Page 265 of the PDF
MrW 4/25
"""

import sys
import pygame
import pygame.font
import random
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet, AlienBullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from background import Background
from powerup import PowerUp


class AlienInvasion:
    """Manages the game and create resources"""

    def __init__(self):
        """Initialized the game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.background = Background(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)
        pygame.display.set_caption("Alien Invasion")
        self.big_shot = False
        self.font = pygame.font.SysFont("magneto", 112)
        # self.font = pygame.font.SysFont("kunstlerscript", 112)
        print(pygame.font.get_fonts())

    def run_game(self):
        """Control the loop for the game"""

        while True:
            # Look for keyboard and mouse events
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._fire_alien_bullet()
                self._update_bullets()
                self._update_aliens()
                self._update_powerups()
                self._update_screen()
            else:
                self._draw_menu()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()

                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            if len(self.aliens) == 1:
                alien.rect.y += 3 * self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # horizantal space
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # vertical space
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (4 * alien_height) - ship_height
        )

        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number

        self.aliens.add(alien)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.alien_bullets.update()
        for bullet in self.alien_bullets.copy():
            if bullet.rect.bottom >= self.settings.screen_height:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        self._check_bullet_ship_collision()

    def _update_powerups(self):
        self.powerups.update()
        for powerup in self.powerups.copy():
            if powerup.rect.bottom >= self.settings.screen_height:
                self.powerups.remove(powerup)
        self._check_ship_powerup_collisions()

    def _check_bullet_ship_collision(self):
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Check if any bullets hit aliens
        # If so, get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:

            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()
            for collision in collisions:
                x = collisions[collision][0].rect.centerx
                y = collisions[collision][0].rect.bottom

            self._roll_for_powerup(x, y)

            if len(self.aliens) == 1:
                for alien in self.aliens:
                    alien.change_color()
                    alien.get_mad()

        # There are no aliens left
        if not self.aliens:

            self._prep_level()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _roll_for_powerup(self, x, y):
        r = random.randint(0, self.settings.powerup_frequency)
        if r == 0:
            self.drop_powerup(x, y)

    def _check_ship_powerup_collisions(self):
        if pygame.sprite.spritecollideany(self.ship, self.powerups):
            self._power_up()
            for powerup in self.powerups:
                powerup.kill()

    def _check_events(self):
        """Check events in the game"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start the game"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()

            self.sb.prep_level()
            self.sb.prep_score()
            self.sb.prep_ships()

            self.stats.game_active = True

            # Get rid of any extra aliens/bullets

            self._prep_level()
            pygame.mouse.set_visible(False)

    def _update_aliens(self):
        """Updates the position of all aliens"""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens hit the bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Responds to aliens hitting the ship"""
        # Lose a life
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # Get rid of any aliens and bullets
            self._prep_level()
            # Pause for a half second
            sleep(0.5)

        else:
            # Game over
            self.stats.game_active = False
            if self.stats.new_high_score:
                with open("high_score.txt", "w") as high_score:
                    high_score.write(str(self.stats.high_score))
            pygame.mouse.set_visible(True)

    def _draw_menu(self):
        """Draws menu when game isn't active"""
        self.background.draw_background()
        self.play_button.draw_button()

        self.msg_image = self.font.render(
            "Alien Invasion",
            True,
            (255, 255, 255),
        )

        self.screen.blit(
            self.msg_image,
            (
                (self.settings.screen_width - self.msg_image.get_width()) / 2,
                self.settings.screen_height / 4,
            ),
        )
        pygame.display.flip()

    def _update_screen(self):
        """Updates images and flips the screen"""
        self.background.draw_background()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        for powerup in self.powerups.sprites():
            powerup.draw()
        # if not self.stats.game_active:
        #    self.play_button.draw_button()

        self.sb.show_score()
        # displays the screen
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if not self.stats.game_active and event.key == pygame.K_p:
            self.stats.game_active = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move ship right
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the group"""
        if self.big_shot:
            self.settings.bullet_width = 1000
            self.big_shot = False

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.bullet_width = 3

    def _fire_alien_bullet(self):
        """Create a new bullet and add it to the group"""
        for alien in self.aliens:
            if alien.roll_to_shoot():
                new_bullet = AlienBullet(self, alien)
                self.alien_bullets.add(new_bullet)

    def drop_powerup(self, x, y):
        new_powerup = PowerUp(self, x, y)
        self.powerups.add(new_powerup)

    def _prep_level(self):
        self.aliens.empty()
        self.bullets.empty()
        self.alien_bullets.empty()
        # Create a new fleet, and center the ship
        self._create_fleet()
        self.ship.center_ship()

    def _power_up(self):
        self.big_shot = True


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
