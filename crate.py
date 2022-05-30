import pygame
from main_destroyable_block import *


class Crate(Main_destroyable_block):

    def __init__(self, x, y):
        super().__init__(x, y, 128)
