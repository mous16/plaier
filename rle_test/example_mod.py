#!/usr/bin/env python
import sys
from random import randrange
from PIL import Image
import numpy

from rle_python_interface.rle_python_interface import RLEInterface

rom_file = "/home/mous16/projects/plaier/data/super_mario_world.sfc"

rle = RLEInterface()

rle.setInt(b'random_seed', 123)

USE_SDL = True
if USE_SDL:
    if sys.platform == 'darwin':
        import pygame
        pygame.init()
        rle.setBool(b'sound', b'false') # Sound doesn't work on OSX
    elif sys.platform.startswith('linux'):
        rle.setBool(b'sound', b'true')
    rle.setBool(b'display_screen', b'true')

rle.loadROM(rom_file, 'snes')

action_right = 128


def advance(rle, total_reward):
    reward = rle.act(action_right)
    total_reward += reward
    return total_reward, reward


def display(rle, title):
    screen = rle.getScreenRGB()
    image = Image.fromarray(screen)
    image.show(title)


total_reward = reward = 0

for i in range(30):
    total_reward, reward = advance(rle, total_reward)
display(rle, "30")

total_reward, reward = advance(rle, total_reward)
display(rle, "31")

total_reward, reward = advance(rle, total_reward)
display(rle, "32")
