from constants import *
from main_enemy_entity import *



class Enemy_0(Main_enemy_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = pygame.math.Vector2()
