from constants import *
import pygame, border_block, crate, random, floor_tile, enemy_1
import convert_csv

class Map:

    def __init__(self, main_group):
        self.levels = ["level_0.csv", "level_1.csv"]

        self.crates_group = main_group.get_group("crates_group")
        self.floor_tiles_group = main_group.get_group("floor_tiles_group")
        self.border_group = main_group.get_group("border_group")
        self.enemy_group = main_group.get_group("enemy_group")

        self.load_level(0, main_group)
        self.add_enemys()

    def load_level(self, level, main_group):


        self.border_group.empty()
        self.floor_tiles_group.empty()

        map_tiles = convert_csv.Convert_csv(self.levels[level]).get_list()
        for row in range(len(map_tiles)):

            for col in range(len(map_tiles[row])):
                item = int(map_tiles[row][col]) // SPRITESHEET_NUM_OF_COLS
                if item == 0:
                    self.border_group.add(border_block.Border_block(col * BLOCK_SIZE, row * BLOCK_SIZE))
                elif item == 7:
                    self.floor_tiles_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 7 * BLOCK_SIZE))
                elif item == 8:
                    self.floor_tiles_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 8 * BLOCK_SIZE))
                elif item == 9:
                    self.floor_tiles_group.add(floor_tile.Floor_tile(col * BLOCK_SIZE, row * BLOCK_SIZE, 9 * BLOCK_SIZE))

        self.add_crates(main_group)


    def add_crates(self, main_group):
        bad_locations = [
            (1, 1), (1, 2), (2, 1),
            (12, 1), (13, 1), (13, 2),
            (12, 9), (13, 9), (13, 8),
            (1, 8), (1, 9), (2, 9)
        ]

        groups = [self.crates_group, self.floor_tiles_group, self.border_group]
        ammount = random.randint(round((ROWS * COLS) * CRATES_LOWER_LIMIT), round((ROWS * COLS) * CRATES_TOP_LIMIT))

        while ammount > 0:
            # print(self.crates_group)
            x = random.randint(1, COLS - 2)
            y = random.randint(1, ROWS - 2)

            if (x, y) not in bad_locations:
                for group in groups:
                    for sprite in group:
                        if not sprite.rect.colliderect(pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)):
                            self.crates_group.add(crate.Crate(x * BLOCK_SIZE, y * BLOCK_SIZE))
                            ammount += -1
                            break
                    else:
                        continue
                    break



    def add_enemys(self):
        self.enemy_group.add(enemy_1.Enemy_1(13 * BLOCK_SIZE, 9 * BLOCK_SIZE))
