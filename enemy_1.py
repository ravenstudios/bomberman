from constants import *
from main_enemy_entity import *



class Enemy_1(Main_enemy_entity):

    def __init__(self, x, y):
        y_sprite_sheet_index = 10 * BLOCK_SIZE
        super().__init__(x, y, y_sprite_sheet_index)
