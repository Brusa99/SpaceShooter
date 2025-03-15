import random

import pygame as pg


class Meteor(pg.sprite.Sprite):
    def __init__(self, display:pg.Surface, image: pg.Surface, pos: tuple[float, float], *groups):
        """Get a meteor entity."""
        super().__init__(*groups)
        self.original_image = image
        self.image = image
        self.rect = self.image.get_frect(bottomleft=pos)
        self.mask = pg.mask.from_surface(self.image)
        self.direction = pg.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.uniform(0.2, 0.4)
        self.angle = 0
        self.rotation_speed = random.uniform(0.02, 0.04)
        self.display = display

    def update(self, dt: float):
        """Move the meteor. If off-screen, remove it."""
        self.rect.center += self.direction * self.speed * dt
        self.angle = (self.angle + self.rotation_speed * dt) % 360
        self.image = pg.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_frect(center=self.rect.center)
        if self.rect.top > self.display.get_height():
            self.kill()


class Explosion(pg.sprite.Sprite):
    def __init__(self, frames: list[pg.Surface], pos: tuple[float, float], *groups):
        """Get an explosion animation."""
        super().__init__(*groups)
        self.frames = frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_frect(center=pos)

    def update(self, dt: float):
        """Cycle through animation. When complete, remove."""
        self.current_frame = self.current_frame + 0.1 * dt
        if self.current_frame >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.current_frame)]

