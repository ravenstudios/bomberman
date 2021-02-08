from main_block import *
import pygame, border_block, crate, random
class Map:

    def __init__(self):
        self.blocks = pygame.sprite.Group()
        # self.top_limit = 0.40
        # self.bottom_limit = 0.30
        self.top_limit = 0.20
        self.bottom_limit = 0.10
        self.make_map()



    def update(self):
        self.blocks.update()

    def draw(self, surface):
        self.blocks.draw(surface)



    def make_map(self):
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 or (c % 2 == 0 and r % 2 == 0):
                    self.blocks.add(border_block.Border_block(c * BLOCK_SIZE, r * BLOCK_SIZE))

        ammount = random.randint(round((ROWS * COLS) * self.bottom_limit), round((ROWS * COLS) * self.top_limit))

        #crates
        while ammount > 0:
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)

            if (x % 2 != 0 or y % 2 != 0) and x != 0 and x != (COLS - 1) and y != 0 and y != (ROWS - 1):
                # Make sure no creates ant starting point
                if (x != 0 and y != 0) and (x != 1 and y != 0) and (x != 0 and y != 1):
                    self.blocks.add(crate.Crate(x * BLOCK_SIZE, y * BLOCK_SIZE))
                    ammount += -1

    def get_blocks(self):
        return self.blocks

    # def destroy_crate(self, id):
    #     for b in self.blocks:
    #         # print(id(b))
    #         if id == b:
    #             self.blocks.remove(b)

    def reset(self):
        self.blocks = pygame.sprite.Group()
        self.make_map()
