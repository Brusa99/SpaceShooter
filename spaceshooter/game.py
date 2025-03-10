import random
from pathlib import Path

import pygame as pg

RESOLUTION = (1280, 720)
FPS = 60
IMG_PATH = Path(__file__).parent / "resources" / "images"

# Init
pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')
clock = pg.time.Clock()

# Assets
player_surf = pg.image.load(IMG_PATH / "player.png").convert_alpha()
player_rect = player_surf.get_frect(center=(display.get_width() / 2, display.get_height() / 2))
player_direction = pg.math.Vector2()
player_speed = 200

meteor_surf = pg.image.load(IMG_PATH / "meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(display.get_width() / 2, display.get_height() / 2))

laser_surf = pg.image.load(IMG_PATH / "laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, display.get_height() - 20))

star_surf = pg.image.load(IMG_PATH / "star.png").convert_alpha()
star_positions = [
    (
        random.randint(0, display.get_width() - star_surf.get_width()),
        random.randint(0, display.get_height() - star_surf.get_height()),
    )
    for _ in range(20)
]

# Run game
running = True
while running:
    dt = clock.tick(FPS) / 1000

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Input
    keys = pg.key.get_pressed()
    jp_keys = pg.key.get_just_pressed()

    player_direction.x = keys[pg.K_d] - keys[pg.K_a]
    player_direction.y = keys[pg.K_s] - keys[pg.K_w]
    player_direction = player_direction.normalize() if player_direction else player_direction

    if jp_keys[pg.K_SPACE]:
        print("pew pew")

    # Updates
    player_rect.center += player_direction * player_speed * dt
    if player_rect.right >= display.get_width():
        player_rect.right = display.get_width()
    if player_rect.left <= 0:
        player_rect.left = 0
    if player_rect.bottom >= display.get_height():
        player_rect.bottom = display.get_height()
    if player_rect.top <= 0:
        player_rect.top = 0

    # Rendering
    display.fill("darkgray")
    for star_pos in star_positions:
        display.blit(star_surf, star_pos)
    display.blit(meteor_surf, meteor_rect)
    display.blit(laser_surf, laser_rect)
    display.blit(player_surf, player_rect)
    pg.display.update()

pg.quit()
