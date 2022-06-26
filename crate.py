import pygame
from main_destroyable_block import *


class Crate(Main_destroyable_block):

    def __init__(self, x, y):
        super().__init__(x, y, 1)
        self.animation_speed = self.animation_speed / 2

    def highlight(self):
        self.y_sprite_sheet_index = 12
