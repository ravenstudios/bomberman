from constants import *
from main_mob_entity import *
import random, bomb, math
vec2 = pygame.math.Vector2

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
        self.states = ["search", "move", "bomb", "run", "wait"]
        self.state = self.states[0]
        self.goal_loc = (0, 0)
        self.path = []
        self.wait_timer = 0
        self.wait_time = 3000
        # goal 1: stay the fuck alive
        # goal 2: hunt for crate and blow that shit up


    def update(self, groups_manager):
        self.animate()

        if pygame.time.get_ticks() >= self.set_bomb_timer + self.set_bomb_timer_max:
            self.can_set_bomb = True
            # self.state = "search"

        cap_str = "self.loc" + str((self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE)) + "self.goal_loc:" + str((self.goal_loc[0] // BLOCK_SIZE, self.goal_loc[1] // BLOCK_SIZE)) +  self.state
        pygame.display.set_caption(cap_str)

        crates_group = groups_manager.get_group("crates_group")
        collideable_objects = groups_manager.get_group("collideable_objects")
        bombs_group = groups_manager.get_group("bombs_group")
        floor_tiles_group = groups_manager.get_group("floor_tiles_group")
        main_group = [collideable_objects, floor_tiles_group]

        if self.state == "search":
            self.goal_loc = self.search_for_crate(crates_group)
            self.path = self.find_path(collideable_objects)
            self.state = "move"

        if self.state == "move":
            self.move_to_location(self.goal_loc, collideable_objects)
            self.move(collideable_objects)

        if self.state == "bomb":
            self.set_bomb(bombs_group)

        if self.state == "wait":
            if self.wait_timer + self.wait_time < pygame.time.get_ticks():
                self.state = "search"

        # if self.state == "run":
        #     self.run(collideable_objects)

    def run(self):
        pass


    def is_obj_at_loc_collideable(self, loc, collideable_objects):
        for obj in collideable_objects:
            if (obj.rect.x, obj.rect.y) == loc:
                return True
        return False



    def find_path(self, goal, collideable_objects):
        queue = []
        visited_locations = []
        starting_place ={

                "loc": self.get_grid_coords(),
                "distance": 0,
                "parent_location": self.get_grid_coords()
                }
        queue.insert(0, starting_place)

        popped_locations = []
        while queue:

            queue.sort(key = lambda x: x["distance"])
            popped = queue.pop(0)
            # print(f"popped:{popped}")
            loc, distance, parent_location = popped.values()
            popped_values = []
            popped_values.append(popped)
            popped_locations.append(loc)

            # print(f"cords:{x, y} distance:{distance} parent_location{parent_location}")
            dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            for d in dirs:
                new_location = (loc[0] + d[0], loc[1] + d[1])


                new_place = {
                    "loc": new_location,
                    "distance": distance + 1,
                    "parent_location": loc
                }


                if new_location == goal:
                    queue.insert(0,
                    {"loc": new_location,
                    "distance": 0,
                    "parent_location": loc})
                    print(popped_values)
                    return popped_locations

                x, y = new_location
                if x > 0 and x < COLS and y > 0 and y < ROWS and new_location not in popped_locations:

                    # for q in queue:
                    #     if q["loc"] == new_location:
                    #         q["distance"] = distance + 1
                    #         q["parent_location"] = loc
                    # else:
                        queue.insert(0, new_place)



                    # queue.sort(key = lambda x: x["distance"])


    def move_to_location(self, goal, collideable_objects):
        goal_x = goal[0] * BLOCK_SIZE
        goal_y = goal[1] * BLOCK_SIZE
        x, y = self.get_coords()
        # ARRIVED AT LOCATION
        if x == goal_x and y == goal_y:
            if self.path:
                self.path.pop(0)
                if self.path:
                    self.goal_loc = self.path[0]
            else:
                if self.can_set_bomb:
                    self.state = "bomb"
                    return "bomb" #used for unittest

        xdir = self.goal_loc[0] - x
        ydir = self.goal_loc[1] - y
        new_dir = vec2(xdir, ydir)
        self.direction = new_dir
        return new_dir #used for unittest








    def move(self, collideable_objects):
        self.rect.x += self.direction.x * self.speed
        x_obj_hit = self.check_collision(collideable_objects, "horizontal")

        self.rect.y += self.direction.y * self.speed
        y_obj_hit = self.check_collision(collideable_objects, "vertical")

        # if isinstance(y_obj_hit, crate.Crate):
        #     if self.can_set_bomb:
        #         self.state = "bomb"




    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        self.set_bomb_timer = pygame.time.get_ticks()
        self.can_set_bomb = False
        self.state = "wait"
        self.wait_timer = pygame.time.get_ticks()




    def search_for_crate(self, crates_group):
        closest_crate_distance = ((ROWS - 1) * BLOCK_SIZE) + ((COLS - 1) * BLOCK_SIZE) ** 2
        closest_rect = 0

        for crate in crates_group:
            diff_x = self.rect.x - crate.rect.x
            diff_y = self.rect.y - crate.rect.y
            distance = diff_x + diff_y ** 2

            if distance < closest_crate_distance:
                closest_crate_distance = distance
                closest_crate = crate.rect

        loc_to_return = vec2(0, 0)
        cc = closest_crate
        if self.rect.x > cc.x: #right
            loc_to_return = vec2(cc.x + BLOCK_SIZE, cc.y)
        if self.rect.x < cc.x: #left
            loc_to_return = vec2(cc.x - BLOCK_SIZE, cc.y)
        if self.rect.y < cc.y: #up
            loc_to_return = vec2(cc.x, cc.y - BLOCK_SIZE)
        if self.rect.y > cc.y: #down
            loc_to_return = vec2(cc.x, cc.y + BLOCK_SIZE)

        return vec2(loc_to_return.x, loc_to_return.y)



    def reset(self):
        self.state = "search"
        self.rect.topleft = (13 * BLOCK_SIZE, 9 * BLOCK_SIZE)
        self.direction = self.random_direction()



    def random_direction(self):

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        r = random.randint(0, 3)
        return vec2(dirs[r])
