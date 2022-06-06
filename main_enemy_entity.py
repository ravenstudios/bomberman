from constants import *
from main_mob_entity import *


class Main_enemy_entity(Main_mob_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = pygame.math.Vector2()

    def update(self):
        self.animate()
        self.move()

    def move(self):
        pass
