import random

import pygame as pg


class Meteor(pg.sprite.Sprite):
    def __init__(self, display:pg.Surface, image: pg.Surface, pos: tuple[float, float], *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_frect(bottomleft=pos)
        self.direction = pg.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.uniform(0.2, 0.4)
        self.display = display

    def update(self, dt: float):
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > self.display.get_height():
            self.kill()
