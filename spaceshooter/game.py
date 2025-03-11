import random

import pygame as pg

from spaceshooter.constants import RESOLUTION, IMG_PATH, FPS
from spaceshooter.player import Player
from spaceshooter.star import Star
from spaceshooter.meteor import Meteor


# Init
pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')
clock = pg.time.Clock()

# Assets
player_group = pg.sprite.Group()
player = Player(display, player_group)

graphics_group = pg.sprite.Group()
star_image = pg.image.load(IMG_PATH / "star.png").convert_alpha()
for _ in range(20):
    Star(display, star_image, graphics_group)

laser_group = pg.sprite.Group()

# Meteors
meteor_image = pg.image.load(IMG_PATH / "meteor.png").convert_alpha()
meteor_group = pg.sprite.Group()
meteor_event = pg.event.custom_type()
pg.time.set_timer(meteor_event, 500)

# Run game
running = True
while running:
    dt = clock.tick(FPS)

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == meteor_event:
            meteor_x = random.randint(0, display.get_width() - meteor_image.width)
            Meteor(display, meteor_image, (meteor_x, 0), meteor_group)

    # Input
    keys = pg.key.get_pressed()
    jp_keys = pg.key.get_just_pressed()

    # Updates
    player_group.update(keys, jp_keys, dt, laser_group)
    meteor_group.update(dt)
    laser_group.update(dt)

    # Rendering
    display.fill("darkgray")

    graphics_group.draw(display)
    meteor_group.draw(display)
    laser_group.draw(display)
    player_group.draw(display)

    pg.display.update()

pg.quit()
