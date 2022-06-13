from constants import *
from main_entity import *
import pygame,  map, crate

class Bomb(Main_entity):

    def __init__(self, x, y, fire_length):
        self.x = (x // BLOCK_SIZE) * BLOCK_SIZE
        self.y = (y // BLOCK_SIZE) * BLOCK_SIZE
        y_sprite_sheet_index = 11 * BLOCK_SIZE
        super().__init__(self.x, self.y, y_sprite_sheet_index)

        self.start = pygame.time.get_ticks()
        self.fuse = 2000
        self.fire_length = fire_length
        self.fires = []

    def update(self, main_group):
        self.animate()
        border_group = main_group.border_group
        crates_group = main_group.crates_group
        bombs_group = main_group.bombs_group

        self.detonate(border_group, crates_group, bombs_group, self.fire_length)



    def detonate(self, border_group, crates_group, bombs_group, fire_length):

        BS = BLOCK_SIZE
        dirs = [True, True, True, True] #bools for each direction

        # if fuse timer runs out:
        now = pygame.time.get_ticks()
        if now - self.start >= self.fuse:
            bombs_group.remove(self)

            for i in range(self.fire_length):

                # tup for the next fire location
                dirs_tups = [
                            (self.x, self.y - (BS * i)),
                            (self.x + (BS * i), self.y),
                            (self.x, self.y + (BS * i)),
                            (self.x - (BS * i), self.y)
                            ]

                for j in range(len(dirs_tups)):  # n, e, s, t
                    if dirs[j]:
                        f = Fire(dirs_tups[j])


                        hit_crates = pygame.sprite.spritecollide(f, crates_group, False)
                        hit_blocks = pygame.sprite.spritecollide(f, border_group, False)

                        if hit_crates or hit_blocks:
                            dirs[j] = False


                        else:
                            bombs_group.add(f)

                        for hc in hit_crates:
                            bombs_group.add(f)
                            hc.remove()







#######   FIRE   #######
class Fire(Main_entity):
    def __init__(self, coord):
        self.x, self.y = coord
        y_sprite_sheet_index = 12 * BLOCK_SIZE
        super().__init__(self.x, self.y, y_sprite_sheet_index)

        self.start = pygame.time.get_ticks()
        self.life_span = 300





    def update(self, main_group):
        self.animate()
        bombs_group = main_group.bombs_group

        if pygame.time.get_ticks() - self.start >= self.life_span:
            bombs_group.remove(self)
