import pygame as pg

from spaceshooter.constants import IMG_PATH


class Player(pg.sprite.Sprite):
    def __init__(self, display: pg.Surface, *groups):
        """Get the player entity."""
        super().__init__(*groups)
        self.display = display
        self.image = pg.image.load(IMG_PATH / "player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(display.get_width() / 2, display.get_height() / 2))
        self.direction = pg.Vector2()
        self.speed = 0.5

        # Cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def update(self, keys: list[bool], jp_keys: list[bool], dt: float) -> None:
        """Move the player."""
        # Get input
        self.direction.x = keys[pg.K_d] - keys[pg.K_a]
        self.direction.y = keys[pg.K_s] - keys[pg.K_w]
        self.direction = self.direction.normalize() if self.direction else self.direction

        # Update
        self.rect.center += self.direction * self.speed * dt

        # Check boundaries
        if self.rect.right >= self.display.get_width():
            self.rect.right = self.display.get_width()
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.bottom >= self.display.get_height():
            self.rect.bottom = self.display.get_height()
        if self.rect.top <= 0:
            self.rect.top = 0

        # Shooting
        if jp_keys[pg.K_SPACE] and self.can_shoot:
            self.laser_shoot_time = pg.time.get_ticks()
            print("pew pew")
            self.can_shoot = False
        self._laser_timer()

    def _laser_timer(self):
        """Determine if player is able to shoot."""
        if not self.can_shoot:
            current_time = pg.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
