import random

import pygame as pg

from spaceshooter.constants import RESOLUTION, IMG_PATH, FPS
from spaceshooter.player import Player
from spaceshooter.star import Star
from spaceshooter.meteor import Meteor


def display_score():
    current_time = pg.time.get_ticks() // 10
    text_surf = font.render(f"Score: {current_time}", True, "#f0f0f0")
    text_rect = text_surf.get_frect(midbottom=(display.get_width() / 2, display.get_height() - 50))
    pg.draw.rect(display, "#f0f0f0", text_rect.inflate(25, 20).move(0, -5), 5, 10)
    display.blit(text_surf, text_rect)


# Init
pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')
clock = pg.time.Clock()

# Assets
font = pg.font.Font(IMG_PATH / "Oxanium-Bold.ttf", 30)

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

    # Collisions
    pg.sprite.groupcollide(laser_group, meteor_group, True, True)
    if pg.sprite.spritecollide(player, meteor_group, dokill=False, collided=pg.sprite.collide_mask):
        print("dead")

    # Rendering
    display.fill("#3a2e3f")
    graphics_group.draw(display)
    meteor_group.draw(display)
    laser_group.draw(display)
    player_group.draw(display)
    display_score()

    pg.display.update()

pg.quit()
