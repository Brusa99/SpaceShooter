import random

import pygame as pg

from spaceshooter.constants import RESOLUTION, IMG_PATH, SND_PATH, FPS
from spaceshooter.player import Player
from spaceshooter.star import Star
from spaceshooter.meteor import Meteor, Explosion


def display_score():
    current_time = pg.time.get_ticks() // 10
    text_surf = font.render(f"Score: {current_time}", True, "#f0f0f0")
    text_rect = text_surf.get_frect(midbottom=(display.get_width() / 2, display.get_height() - 50))
    pg.draw.rect(display, "#f0f0f0", text_rect.inflate(25, 20).move(0, -5), 5, 10)
    display.blit(text_surf, text_rect)


# Init
pg.init()
pg.mixer.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')
clock = pg.time.Clock()

# Assets
font = pg.font.Font(IMG_PATH / "Oxanium-Bold.ttf", 30)
music = pg.mixer.Sound(SND_PATH / "game_music.wav")
music.set_volume(0.1)
music.play(-1)

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

# Explosion
explosion_frames = [pg.image.load(IMG_PATH / "explosion" / f"{img}.png").convert_alpha() for img in range(21)]
explosion_sound = pg.mixer.Sound(SND_PATH / "explosion.wav")
explosion_sound.set_volume(0.2 )
explosion_group = pg.sprite.Group()

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
    explosion_group.update(dt)

    # Collisions
    for laser in laser_group.sprites():
        collided_sprites = pg.sprite.spritecollide(laser, meteor_group, True)
        if collided_sprites:
            laser.kill()
            Explosion(explosion_frames, laser.rect.midtop, explosion_group)
            explosion_sound.play()
    if pg.sprite.spritecollide(player, meteor_group, dokill=False, collided=pg.sprite.collide_mask):
        print(f"\nGame Over\n\nScore: {pg.time.get_ticks() // 10}")
        running = False

    # Rendering
    display.fill("#3a2e3f")
    graphics_group.draw(display)
    meteor_group.draw(display)
    laser_group.draw(display)
    player_group.draw(display)
    explosion_group.draw(display)
    display_score()

    pg.display.update()

pg.quit()
