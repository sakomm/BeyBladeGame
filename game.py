# rdj5uub - Rahul Jha
import gamebox
import pygame
from pygame.locals import *  #
import random

camera = gamebox.Camera(800, 600)

spaceship = gamebox.from_image(400, 550,
    "https://www.pinclipart.com/picdir/big/339-3399822_spaceship-d600-video-game-spaceship-clipart.png")
spaceship.scale_by(0.07)
left_side = gamebox.from_color(0,600,"black",1,600)
right_side = gamebox.from_color(800,600,"black",1,600)

score = 0
menu = gamebox.from_text(700 + score * 10, 75, "Untitled Space Defenders Knockoff", 40, "purple")
enemy = []
bullets = []
game_end = False
timer = 0


def tick(keys):
    global enemy
    global game_end
    global timer
    global menu

    if game_end:
        timer += 1

    if pygame.K_ESCAPE in keys:
        gamebox.stop_loop()

    if pygame.K_LEFT in keys:
        if not spaceship.left_touches(left_side):
            spaceship.move(-10, 0)

    if pygame.K_RIGHT in keys:
        if not spaceship.right_touches(right_side):
            spaceship.move(10, 0)
    if pygame.K_SPACE in keys:
        shoot()

    camera.clear("black")
    for k in range(len(bullets)):
        bullets[k].move_speed()
        camera.draw(bullets[k])
    camera.draw(spaceship)
    camera.display()


def shoot():
    bullet = gamebox.from_color(spaceship.x, spaceship.y - 60, "red", 10, 20)
    bullet.speedy = -10
    bullets.append(bullet)



gamebox.timer_loop(30, tick)
