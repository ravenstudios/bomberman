from constants import *
import pygame, border_block, crate, random, floor_tile
import convert_csv

class Map:

    def __init__(self, border_group, tile_group):
        self.map = pygame.sprite.Group()
        # self.top_limit = 0.40
        # self.bottom_limit = 0.30
        self.top_limit = 0.20
        self.bottom_limit = 0.10
        # self.map = self.make_map(border_group, tile_group)
        self.levels = ["level_0.csv", "level_1.csv"]
        self.load_level(0, border_group, tile_group)



    def load_level(self, level, border_group, tile_group):
        border_group.empty()
        tile_group.empty()

        map_tiles = convert_csv.Convert_csv(self.levels[level]).get_list()
        for row in range(len(map_tiles)):

            for col in range(len(map_tiles[row])):
                item = int(map_tiles[row][col]) // SPRITESHEET_NUM_OF_COLS
                if item == 0:
                    border_group.add(border_block.Border_block(col * BLOCK_SIZE, row * BLOCK_SIZE))
                elif item == 7:
                    tile_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 7 * BLOCK_SIZE))
                elif item == 8:
                    tile_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 8 * BLOCK_SIZE))
                elif item == 9:
                    tile_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 9 * BLOCK_SIZE))



    def add_crates(self, crates_group):
        ammount = random.randint(round((ROWS * COLS) * self.bottom_limit), round((ROWS * COLS) * self.top_limit))

        #crates
        while ammount > 0:
            x = random.randint(1, COLS - 1)
            y = random.randint(1, ROWS - 1)

            if (x % 2 != 0 or y % 2 != 0) and x != 0 and x != (COLS - 1) and y != 0 and y != (ROWS - 1):
                # Make sure no creates ant starting point
                if (x != 0 and y != 0) and (x != 1 and y != 0) and (x != 0 and y != 1):
                    crates_group.add(crate.Crate(x * BLOCK_SIZE, y * BLOCK_SIZE))
                    ammount += -1
