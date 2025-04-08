import pygame

class JetFighter:
    """A class to manage the JetFighter."""

    def __init__(self, ao_game):
        """Initialize the jet and set its starting position."""
        self.screen = ao_game.screen
        self.screen_rect = ao_game.screen.get_rect()

        # load the jet image and get its rect.
        self.image = pygame.image.load('/Users/quanefiom/desktop/python_work/chapters/Chp12_Alien_Invasion/Exercises/smallfighter-preview.bmp')
        self.rect = self.image.get_rect()

        # Start each new jet at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the jet at its current location."""
        self.screen.blit(self.image, self.rect)