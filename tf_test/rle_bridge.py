import sys
from random import randrange
from PIL import Image
import numpy

from rle_python_interface.rle_python_interface import RLEInterface

from enum import IntEnum


class RLEManager():
    rom_file = "/home/mous16/projects/plaier/data/super_mario_world.sfc"

    def __init__(self, seed=123, use_sdl=True):
        self.rle = RLEInterface()
        self.rle.setInt(b'random_seed', seed)
        if use_sdl:
            if sys.platform == 'darwin':
                import pygame
                pygame.init()
                self.rle.setBool(b'sound', b'false') # Sound doesn't work on OSX
            elif sys.platform.startswith('linux'):
                self.rle.setBool(b'sound', b'true')
            self.rle.setBool(b'display_screen', b'true')

    def start(self):
        self.rle.loadROM(RLEManager.rom_file, 'snes')

    def advance(self, total_reward, action, repetition=1, rewards=[]):
        reward = self.rle.act(action)
        total_reward += reward
        rewards.append(reward)

        if repetition == 1:
            return total_reward, rewards
        else:
            return self.advance(total_reward, action, repetition-1, rewards)

    def show(self, title):
        screen = self.rle.getScreenRGB()

        
    def screen(self, color=True):
        return self.rle.getScreenRGB() if color else self.rle.getScreen()


class RLEActions(IntEnum):
    Noop            = 0b0
    B               = 0b1
    Y               = 0b10
    Select          = 0b100
    Start           = 0b1000
    Up              = 0b10000
    Down            = 0b100000
    Left            = 0b1000000
    Right           = 0b10000000
    A               = 0b100000000
    X               = 0b1000000000
    L               = 0b10000000000
    R               = 0b100000000000
    L2              = 0b1000000000000
    R2              = 0b10000000000000
    L3              = 0b100000000000000
    R3              = 0b1000000000000000
    Reset           = 0b10000000000000000
    Undefined       = 0b100000000000000000
    Random          = 0b1000000000000000000
    SaveState       = 0b10000000000000000000
    LoadState       = 0b100000000000000000000
    SystemReset     = 0b1000000000000000000000
    LastActionIndex = 0b10000000000000000000000


class LeftInputs(IntEnum):
    Noop = RLEActions.Noop
    Up = RLEActions.Up
    Down = RLEActions.Down
    Left = RLEActions.Left
    Right = RLEActions.Right
    UpLeft = RLEActions.Up | RLEActions.Left
    UpRight = RLEActions.Up | RLEActions.Right
    DownLeft = RLEActions.Down | RLEActions.Left
    DownRight = RLEActions.Down | RLEActions.Right


class RightInputs(IntEnum):
    Noop = RLEActions.Noop
    B = RLEActions.B
    Y = RLEActions.Y
    A = RLEActions.A
    X = RLEActions.X
    BY = RLEActions.B | RLEActions.Y
    AX = RLEActions.A | RLEActions.X
    

