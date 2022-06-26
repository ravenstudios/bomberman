from main_non_destroyable_block import *

class Border_block(Main_non_destroyable_block):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.animation_speed = 0.01
