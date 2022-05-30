import pygame
from main_entity import *


class Main_destroyable_block(Main_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.can_remove = False
        self.life_span_after_removal = 300
        self.timer_to_remove_start = 0


    def update(self):
        self.animate()
        now = pygame.time.get_ticks()
        
        if self.can_remove and self.timer_to_remove_start + self.life_span_after_removal < now:
            self.kill()



    def remove(self):
        self.can_remove = True
        self.timer_to_remove_start = pygame.time.get_ticks()
