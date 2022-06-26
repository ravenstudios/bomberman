from constants import *
from main_mob_entity import *
import random, bomb
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

        cap_str = "self.loc" + str((self.rect.x // BLOCK_SIZE, self.rect.y // BLOCK_SIZE)) + "self.goal_loc:" + str((self.goal_loc[0], self.goal_loc[1])) +  self.state
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



    def find_path(self, collideable_objects):

        visited_places = []
        queue = []
        queue.insert(0, self.get_coords())

        while queue:
            current = queue.pop(0)
            # print(f"current: {current} goal_loc:{self.goal_loc}")
            visited_places.append(current)
            if current == self.goal_loc:
                return visited_places

            dirs = [vec2(0,-BLOCK_SIZE), vec2(BLOCK_SIZE,0), vec2(0,BLOCK_SIZE), vec2(-BLOCK_SIZE,0)]

            for d in dirs:
                x = current[0] + d.x
                y = current[1] + d.y
                # print(f"x:{x} y:{y}")
                if x >= 0 and y >= 0 and x <= COLS * BLOCK_SIZE and y <= ROWS * BLOCK_SIZE:
                    loc = (x, y)

                if not self.is_obj_at_loc_collideable(loc, collideable_objects) and loc not in visited_places:
                    queue.insert(0, loc)
                    if loc == self.goal_loc:
                        return visited_places


    def move_to_location(self, goal, collideable_objects):
        goal_x = goal[0] * BLOCK_SIZE
        goal_y = goal[1] * BLOCK_SIZE
        x, y = self.get_coords()
        # ARRIVED AT LOCATION
        print(f"goal_x:{goal_x} goal_y:{goal_y} x:{x} y:{y}")
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

    # pos = vec2(self.x, self.y)
    # enemy = min([e for e in enemies], key=lambda e: pos.distance_to(vec2(e.x, e.y)))

        closest_crate_loc = 10000
        closest_crate_loc_rect = vec2(0, 0)
        self_loc = vec2(self.rect.x, self.rect.y)
        closest_crate = 0

        for crate in crates_group:
            crate_loc = vec2(crate.rect.x, crate.rect.y)
            if crate_loc.distance_to(self_loc) < closest_crate_loc:
                closest_crate_loc = crate_loc.distance_to(self_loc)
                closest_crate_loc_rect = crate.rect
                closest_crate = crate

        result_loc = (closest_crate_loc_rect.x // BLOCK_SIZE, closest_crate_loc_rect.y // BLOCK_SIZE)
        # closest_crate.highlight()
        print("result:", result_loc)
        if self.rect.x > closest_crate_loc_rect.x:#right
            print(((closest_crate_loc_rect.x // BLOCK_SIZE) + 1, (closest_crate_loc_rect.y // BLOCK_SIZE)))
            return ((closest_crate_loc_rect.x // BLOCK_SIZE) + 1, (closest_crate_loc_rect.y // BLOCK_SIZE))
        if self.rect.x < closest_crate_loc_rect.x:#left
            print(((closest_crate_loc_rect.x // BLOCK_SIZE) - 1, (closest_crate_loc_rect.y // BLOCK_SIZE)))
            return ((closest_crate_loc_rect.x // BLOCK_SIZE) - 1, (closest_crate_loc_rect.y // BLOCK_SIZE))
        if self.rect.y > closest_crate_loc_rect.y:#down
            print(((closest_crate_loc_rect.x // BLOCK_SIZE), (closest_crate_loc_rect.y // BLOCK_SIZE) + 1))
            return ((closest_crate_loc_rect.x // BLOCK_SIZE), (closest_crate_loc_rect.y // BLOCK_SIZE) + 1)
        if self.rect.y < closest_crate_loc_rect.y:#up
            print(((closest_crate_loc_rect.x // BLOCK_SIZE), (closest_crate_loc_rect.y // BLOCK_SIZE) - 1))
            return ((closest_crate_loc_rect.x // BLOCK_SIZE), (closest_crate_loc_rect.y // BLOCK_SIZE) - 1)




    def reset(self):
        self.state = "search"
        self.rect.topleft = (13 * BLOCK_SIZE, 9 * BLOCK_SIZE)
        self.direction = self.random_direction()



    def random_direction(self):

        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        r = random.randint(0, 3)
        return vec2(dirs[r])
