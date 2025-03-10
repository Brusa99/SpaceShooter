import random

import pygame as pg

from spaceshooter.constants import RESOLUTION, IMG_PATH, FPS
from spaceshooter.player import Player
from spaceshooter.star import Star


# Init
pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')
clock = pg.time.Clock()

# Assets
all_sprites = pg.sprite.Group()

player = Player(display, all_sprites)

star_image = pg.image.load(IMG_PATH / "star.png").convert_alpha()
for _ in range(20):
    Star(display, star_image, all_sprites)

meteor_surf = pg.image.load(IMG_PATH / "meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(display.get_width() / 2, display.get_height() / 2))

laser_surf = pg.image.load(IMG_PATH / "laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, display.get_height() - 20))

# Run game
running = True
while running:
    dt = clock.tick(FPS)

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Input
    keys = pg.key.get_pressed()
    jp_keys = pg.key.get_just_pressed()

    if jp_keys[pg.K_SPACE]:
        print("pew pew")

    # Updates
    all_sprites.update(keys, dt)

    # Rendering
    display.fill("darkgray")
    display.blit(meteor_surf, meteor_rect)
    display.blit(laser_surf, laser_rect)

    all_sprites.draw(display)

    pg.display.update()

pg.quit()
