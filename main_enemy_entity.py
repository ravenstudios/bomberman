from constants import *
from main_mob_entity import *
import random, crate, bomb, border_block

class Main_enemy_entity(Main_mob_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = pygame.math.Vector2(-1, 0)
        self.speed = 3
        self.fire_length = 3



    def update(self, groups_manager):
        collideable_objects = groups_manager.get_group("collideable_objects")
        crates_group = groups_manager.get_group("crates_group")
        bombs_group = groups_manager.get_group("bombs_group")
        border_group = groups_manager.get_group("border_group")

        # collideable_objects.empty()
        # collideable_objects.add(crates_group, border_group)

        self.animate()

        self.ai(collideable_objects, crates_group, bombs_group)


    def ai(self, collideable_objects, crates_group, bombs_group):

        for sprite in collideable_objects:
            next_step = sprite.rect.colliderect(self.rect.move(0, self.rect.x + self.direction.x * self.speed))
            if not next_step:
                self.rect.x += self.direction.x * self.speed
            else:
                if self.direction.x > 0:
                    self.rect.right = next_step.rect.left
                elif self.direction.x < 0:
                    self.rect.left = next_step.rect.right
            next_step = sprite.rect.colliderect(self.rect.move(0, self.rect.y + self.direction.y * self.speed))
            if not next_step:
                self.rect.y += self.direction.y * self.speed
            else:
                if self.direction.y > 0:
                    self.rect.bottom = next_step.rect.top
                elif self.direction.y < 0:
                    self.rect.top = next_step.rect.bottom

        # x_collision = self.check_collision(collideable_objects, "horizontal")
        #
        # self.rect.y += self.direction.y * self.speed
        # y_collision = self.check_collision(collideable_objects, "vertical")
        #
        # if x_collision or y_collision:
        #     if type(x_collision) == crate.Crate or type(y_collision) == crate.Crate:
        #         self.direction = pygame.math.Vector2(0, 0)
        #         bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        #         escape_locations = self.get_escape_locations(self.rect)
        #
        #         for sprite in collideable_objects:
        #             for location in escape_locations:
        #                 if sprite.rect.x == location[0] and sprite.rect.y == location[1]:
        #                     escape_locations.remove(location)
        #
        #         if escape_locations:
        #             # self.rect.x = escape_locations[0][0]
        #             # self.rect.y = escape_locations[0][1]
        #             self.direction = self.random_direction()
        #             return
        #         else:
        #             self.direction = self.random_direction()
        #             return
        #
        #     elif type(x_collision) == border_block.Border_block or type(y_collision) == border_block.Border_block:
        #         self.direction = self.random_direction()
        #         return
        #     # elif type(y_collision) == border_block.Border_block:
        #     #     self.direction.y = -self.direction.y
        #     #     return
        #
        #





    def get_escape_locations(self, rect):
        return  [
            ((rect.x - BLOCK_SIZE), (rect.y - BLOCK_SIZE)),
            ((rect.x + BLOCK_SIZE), (rect.y - BLOCK_SIZE)),
            ((rect.x + BLOCK_SIZE), (rect.y + BLOCK_SIZE)),
            ((rect.x - BLOCK_SIZE), (rect.y + BLOCK_SIZE))
            ]


    def random_direction(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = random.randint(0, 3)
        return pygame.math.Vector2(dirs[r])
