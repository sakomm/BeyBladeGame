import os
import sys
import time

import pygame
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # prepriping info gathering

pygame.init()
pygame.font.init()

screenInfo = pygame.display.Info()  # grabbing
Screen_Width = screenInfo.current_w
Screen_Height = screenInfo.current_h
screen = pygame.display.set_mode(
    (Screen_Width, Screen_Height))  # set size here


def Info():
    while True:
        screen.fill([69,72,165])

