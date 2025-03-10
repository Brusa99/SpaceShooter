import random

import pygame as pg


class Star(pg.sprite.Sprite):
    def __init__(self, display: pg.Surface, image: pg.Surface, *groups):
        """Get a star sprite."""
        super().__init__(*groups)
        self.image = image

        # Assign random position
        x = random.randint(0, display.get_width() - self.image.get_width())
        y = random.randint(0, display.get_height() - self.image.get_height())
        self.rect = self.image.get_rect(topleft=(x, y))
