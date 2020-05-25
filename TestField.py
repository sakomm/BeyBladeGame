import pygame as pg

pg.init()
screen = pg.display.set_mode((500,500))
Exit_Event = False

while not Exit_Event:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True

        pg.display.flip()
