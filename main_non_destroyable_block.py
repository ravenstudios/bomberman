import pygame
from main_entity import *


class Main_non_destroyable_block(Main_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)

    def update(self):
        self.animate()
