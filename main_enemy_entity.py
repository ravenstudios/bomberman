from constants import *
from main_mob_entity import *
import random, crate, bomb, border_block

class Main_enemy_entity(Main_mob_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = self.random_direction()
        self.speed = 3
        self.fire_length = 3
        self.set_bomb_timer = 0
        self.can_set_bomb = True
        self.set_bomb_timer_max = 2000
        self.hitbox = self.rect.inflate(-10, -10)
        self.states = ["search", "move", "bomb", "run"]
        self.state = self.states[0]
        self.goal_loc = self.rect
        # goal 1: stay the fuck alive
        # goal 2: hunt for crate and blow that shit up

    def update(self, groups_manager):

        self.animate()


        if pygame.time.get_ticks() >= self.set_bomb_timer + self.set_bomb_timer_max:
            self.can_set_bomb = True

        cap_str = "self.loc" + str((self.rect.x // 64, self.rect.y // 64)) + "self.goal_loc:" + str((self.goal_loc[0] // 64, self.goal_loc[1] // 64)) +  self.state

        pygame.display.set_caption(cap_str)
        crates_group = groups_manager.get_group("crates_group")
        collideable_objects = groups_manager.get_group("collideable_objects")
        bombs_group = groups_manager.get_group("bombs_group")
        # self.search_for_crate(crates_group)

        if self.state == "search":
            self.goal_loc = self.search_for_crate(crates_group)
            if self.goal_loc:
                self.state = "move"

        if self.state == "move":
            self.move_to_location(self.goal_loc, collideable_objects)


        if self.state == "bomb":
            self.set_bomb(bombs_group)

        if self.state == "run":
            self.run(bombs_group, collideable_objects)




    def run(self, bombs_group, collideable_objects):

        # find the nearest diagonal spot that is'nt collideable and set goal_loc
        closest_safe_spot = 0
        closest_safe_spot_vector = (0, 0)
        self_loc = self.rect.x + self.rect.y

        for obj in collideable_objects:
            obj_loc = obj.rect.x + obj.rect.y
            if obj_loc < self_loc and obj_loc > closest_safe_spot:
                closest_safe_spot = obj_loc
                closest_safe_spot_vector = obj.rect

        self.goal_loc = closest_safe_spot_vector
        self.state = "move"



    def move_to_location(self, location, collideable_objects):
        if self.rect.x == location.x and self.rect.y == location.y:
            self.state = "search"
        # horizontal
        if self.rect.x > location.x:
            self.direction = pygame.math.Vector2(-1, 0)
        elif self.rect.x < location.x:
            self.direction = pygame.math.Vector2(1, 0)

        self.rect.x += self.direction.x * self.speed
        x_obj_hit = self.check_collision(collideable_objects, "horizontal")
        if isinstance(x_obj_hit, crate.Crate):
            if self.can_set_bomb:
                self.state = "bomb"


        # vertical
        if self.rect.y > location.y:
            self.direction = pygame.math.Vector2(0, -1)
        elif self.rect.y < location.y:
            self.direction = pygame.math.Vector2(0, 1)

        self.rect.y += self.direction.y * self.speed
        y_obj_hit = self.check_collision(collideable_objects, "vertical")
        if isinstance(y_obj_hit, crate.Crate):
            if self.can_set_bomb:
                self.state = "bomb"
        



    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        self.set_bomb_timer = pygame.time.get_ticks()
        self.can_set_bomb = False
        self.state = "run"



    def search_for_crate(self, crates_group):
        closest_crate_loc = 0
        closest_crate_loc_vector = (0, 0)
        self_loc = self.rect.x + self.rect.y

        for crate in crates_group:
            crate_loc = crate.rect.x + crate.rect.y
            if crate_loc < self_loc and crate_loc > closest_crate_loc:
                closest_crate_loc = crate_loc
                closest_crate_loc_vector = crate.rect
        return closest_crate_loc_vector



    def reset(self):
        self.state = "search"
        self.rect.topleft = (13 * BLOCK_SIZE, 9 * BLOCK_SIZE)
        self.direction = self.random_direction()



    def random_direction(self):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = random.randint(0, 3)
        return pygame.math.Vector2(dirs[r])
