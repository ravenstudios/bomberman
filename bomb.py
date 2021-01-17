from constants import *
from main_block import *
import pygame, main_block

class Bomb(main_block.Main_block):

    def __init__(self, x, y):
        self.x = (x // BLOCK_SIZE) * BLOCK_SIZE
        self.y = (y // BLOCK_SIZE) * BLOCK_SIZE
        super().__init__(self.x, self.y)
        self.can_destroy = False
        self.start = pygame.time.get_ticks()
        self.fuse = 1000

    def update(self, objects):
        now = pygame.time.get_ticks()
        if now - self.start >= self.fuse:
            self.can_destroy = True


    def draw(self, surface):
        bs = BLOCK_SIZE // 2
        if not self.can_destroy:
            pygame.draw.circle(surface, (100, 100, 100), (self.x + bs, self.y + bs), bs)
