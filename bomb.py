from constants import *
from main_block import *
import pygame, main_block, map, crate

class Bomb(main_block.Main_block):

    def __init__(self, x, y, fire_length):
        self.x = (x // BLOCK_SIZE) * BLOCK_SIZE
        self.y = (y // BLOCK_SIZE) * BLOCK_SIZE

        super().__init__(self.x, self.y, 3 * BLOCK_SIZE)

        self.start = pygame.time.get_ticks()
        self.fuse = 1000
        self.fire_length = fire_length
        self.fires = []

    def update(self, bombs_group, map_group):


        self.detonate(map_group, bombs_group, self.fire_length)



    def detonate(self, map_group, bombs_group, fire_length):
        bs = BLOCK_SIZE

        # if fuse timer runs out:
        now = pygame.time.get_ticks()
        if now - self.start >= self.fuse:
            bombs_group.remove(self)

            for i in range(self.fire_length):
                n = Fire(self.x, self.y - (bs * i))
                s = Fire(self.x, self.y + (bs * i))
                e = Fire(self.x + (bs * i), self.y)
                w = Fire(self.x - (bs * i), self.y)
                bombs_group.add(n)
                bombs_group.add(s)
                bombs_group.add(e)
                bombs_group.add(w)



        pygame.sprite.groupcollide(bombs_group, map_group, True, False)



#######   FIRE   #######
class Fire(main_block.Main_block):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, 1 * BLOCK_SIZE)

        self.start = pygame.time.get_ticks()
        self.life_span = 300





    def update(self, bombs_group, map_group):
        if pygame.time.get_ticks() - self.start >= self.life_span:
            bombs_group.remove(self)
