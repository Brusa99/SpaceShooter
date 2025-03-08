import pygame as pg

RESOLUTION = (1280, 720)


pg.init()
display = pg.display.set_mode(RESOLUTION)
pg.display.set_caption('Space Shooter')


running = True
while running:
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Rendering
    pg.display.update()

pg.quit()
