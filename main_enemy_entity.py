from constants import *
from main_mob_entity import *
import random, crate, bomb, border_block

class Main_enemy_entity(Main_mob_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = self.random_direction()
        self.speed = 3
        self.fire_length = 3
        self.hitbox = self.rect.inflate(-10, -10)



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
        pygame.display.set_caption(str(self.rect))


        for sprite in collideable_objects:

            if sprite.rect.colliderect(self.rect.move(self.direction.x * self.speed, 0)):


                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    self.direction = self.random_direction()
                    # return
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.direction = self.random_direction()

                if type(sprite) == crate.Crate:
                    bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))

        self.rect.x += self.direction.x * self.speed

        for sprite in collideable_objects:

            if sprite.rect.colliderect(self.rect.move(0, self.direction.y * self.speed)):

                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction = self.random_direction()
                    # return
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction = self.random_direction()

                if type(sprite) == crate.Crate:
                    bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))

        self.rect.y += self.direction.y * self.speed






    def reset(self):
        self.rect.topleft = (13 * BLOCK_SIZE, 9 * BLOCK_SIZE)
        self.direction = self.random_direction()



    def random_direction(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = random.randint(0, 3)
        return pygame.math.Vector2(dirs[r])
