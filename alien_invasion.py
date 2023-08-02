import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event.key)

    def _check_keydown_events(self, key):
        """Respond to keypresses"""
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.ship.moving_right = True
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.ship.moving_left = True
        elif key == pygame.K_UP or key == pygame.K_w:
            self.ship.moving_up = True
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.ship.moving_down = True
        elif key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, key):
        """Respond to key releases."""
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.ship.moving_right = False
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.ship.moving_left = False
        elif key == pygame.K_UP or key == pygame.K_w:
            self.ship.moving_up = False
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.ship.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
