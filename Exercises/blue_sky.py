# Exercise 12-2: Display a jet fighter on the game screen. 
import sys

import pygame

from f15_settings import JetSettings
from f15 import JetFighter
class AirforceOne:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.f15_settings = JetSettings()

        self.screen = pygame.display.set_mode((self.f15_settings.screen_width, self.f15_settings.screen_height))
        pygame.display.set_caption("Airforce One")

        self.f15 = JetFighter(self)

        # Set a blue background color.
        self.bg_color = (0, 120, 210)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.f15_settings.bg_color)
        self.f15.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ao = AirforceOne()
    ao.run_game()
