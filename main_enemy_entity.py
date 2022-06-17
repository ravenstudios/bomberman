from constants import *
from main_mob_entity import *
import random, crate, bomb, border_block

class Main_enemy_entity(Main_mob_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = self.random_direction()
        self.speed = 1
        self.fire_length = 3
        self.set_bomb_timer = 0
        self.can_set_bomb = True
        self.set_bomb_timer_max = 2900
        self.hitbox = self.rect.inflate(-10, -10)
        self.states = ["search", "move", "bomb", "run"]
        self.state = self.states[0]
        self.goal_loc = (8, 8)
        self.path = []
        # goal 1: stay the fuck alive
        # goal 2: hunt for crate and blow that shit up


    def update(self, groups_manager):

        self.animate()


        if pygame.time.get_ticks() >= self.set_bomb_timer + self.set_bomb_timer_max:
            self.can_set_bomb = True
            # self.state = "search"

        cap_str = "self.loc" + str((self.rect.x, self.rect.y)) + "self.goal_loc:" + str((self.goal_loc[0], self.goal_loc[1])) +  self.state

        pygame.display.set_caption(cap_str)
        crates_group = groups_manager.get_group("crates_group")
        collideable_objects = groups_manager.get_group("collideable_objects")
        bombs_group = groups_manager.get_group("bombs_group")
        floor_tiles_group = groups_manager.get_group("floor_tiles_group")
        main_group = [collideable_objects, floor_tiles_group]
        # self.search_for_crate(crates_group)

        if self.state == "search":
            self.path = self.find_path((8, 8), collideable_objects)
            print("search", self.path)
            self.state = "move"

        if self.state == "move":
            self.move_to_location(collideable_objects)


        if self.state == "bomb":
            self.set_bomb(bombs_group)

        # if self.state == "run":
        #     self.run(collideable_objects)

    def run(self):
        pass


    def find_path(self, goal, collideable_objects):
        # print("FIND PATH FUN")
        def is_obj_at_loc_collideable(loc):
            for obj in collideable_objects:
                if (obj.rect.x // 64, obj.rect.y // 64) == loc:
                    return True
            return False


        visited_places = []
        queue = []
        queue.insert(0, self.get_coords())

        while queue:

            current = queue.pop(0)
            visited_places.append(current)
            if current == goal:
                # print(visited_places)
                return visited_places

            dirs = [(0,-1), (1,0), (0,1), (-1,0)]

            for d in dirs:
                x = current[0] + d[0]
                y = current[1] + d[1]
                loc = (x, y)
                if not is_obj_at_loc_collideable(loc) and loc not in visited_places:
                    queue.insert(0, loc)




    def move_to_location(self, collideable_objects):
        goal_x = self.path[0][0] * BLOCK_SIZE
        goal_y = self.path[0][1] * BLOCK_SIZE

        # ARRIVED AT LOCATION
        if self.rect.x == goal_x and self.rect.y == goal_y:
            # self.state = "search"

            self.path.pop(0)

            self.goal_loc = self.path[0]
            return



        # horizontal
        if self.rect.x > goal_x:
            self.direction = pygame.math.Vector2(-1, 0)
        elif self.rect.x < goal_x:
            self.direction = pygame.math.Vector2(1, 0)

        self.rect.x += self.direction.x * self.speed
        x_obj_hit = self.check_collision(collideable_objects, "horizontal")
        # if isinstance(x_obj_hit, crate.Crate):
        #     if self.can_set_bomb:
        #         self.state = "bomb"

        # elif isinstance(x_obj_hit, border_block.Border_block):
        #     self.direction = self.random_direction()


        # vertical
        if self.rect.y > goal_y:
            self.direction = pygame.math.Vector2(0, -1)
        elif self.rect.y < goal_y:
            self.direction = pygame.math.Vector2(0, 1)

        self.rect.y += self.direction.y * self.speed
        y_obj_hit = self.check_collision(collideable_objects, "vertical")

        # if isinstance(y_obj_hit, crate.Crate):
        #     if self.can_set_bomb:
        #         self.state = "bomb"
        # elif isinstance(y_obj_hit, border_block.Border_block):
        #     self.direction = self.random_direction()




    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        self.set_bomb_timer = pygame.time.get_ticks()
        self.can_set_bomb = False
        self.state = "run"



    def search_for_crate(self, crates_group):
        closest_crate_loc = 0
        closest_crate_loc_rect = self.rect
        self_loc = self.rect.x + self.rect.y

        for crate in crates_group:
            crate_loc = crate.rect.x + crate.rect.y
            if crate_loc < self_loc and crate_loc > closest_crate_loc:
                closest_crate_loc = crate_loc
                closest_crate_loc_rect = crate.rect
        return closest_crate_loc_rect



    def reset(self):
        self.state = "search"
        self.rect.topleft = (13 * BLOCK_SIZE, 9 * BLOCK_SIZE)
        self.direction = self.random_direction()



    def random_direction(self):

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        r = random.randint(0, 3)
        return pygame.math.Vector2(dirs[r])



class Path_finding:
    def __init__(self, entity, map):
        self.map = map
        self.rect = entity.rect
        self.x = self.rect.x // 64
        self.y = self.y.rect // 64

    def find_path(self):
        pass
