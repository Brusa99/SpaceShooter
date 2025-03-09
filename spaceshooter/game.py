import random
from pathlib import Path

import pygame as pg

RESOLUTION = (1280, 720)
IMG_PATH = Path(__file__).parent / "resources" / "images"

# Init
pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')

# Assets
player_surf = pg.image.load(IMG_PATH / "player.png").convert_alpha()
player_rect = player_surf.get_frect(center=(display.get_width() / 2, display.get_height() / 2))
player_direction = 1

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
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Updates
    player_rect.left += 0.1 * player_direction
    if player_rect.right >= display.get_width() or player_rect.left <= 0:
        player_direction *= -1

    # Rendering
    display.fill("darkgray")
    for star_pos in star_positions:
        display.blit(star_surf, star_pos)
    display.blit(meteor_surf, meteor_rect)
    display.blit(laser_surf, laser_rect)
    display.blit(player_surf, player_rect)
    pg.display.update()

pg.quit()
