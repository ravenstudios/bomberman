from constants import *
from main_block import *
import pygame, main_block, map, crate

class Bomb(main_block.Main_block):

    def __init__(self, x, y, fire_length):
        self.x = (x // BLOCK_SIZE) * BLOCK_SIZE
        self.y = (y // BLOCK_SIZE) * BLOCK_SIZE
        super().__init__(self.x, self.y)
        self.can_destroy = False
        self.start = pygame.time.get_ticks()
        self.fuse = 1000
        self.fire_length = fire_length
        self.fires = []

    def update(self, objects):

        # if fuse timer runs out:
        if self.can_destroy == False:
            now = pygame.time.get_ticks()
            if now - self.start >= self.fuse:
                self.detonate(objects, self.fire_length)
                self.can_destroy = True

        # update and remove  all fires
        for fire in self.fires:
            fire.update(objects)
            if fire.can_destroy:
                self.fires.remove(fire)

    def draw(self, surface):
        bs = BLOCK_SIZE // 2
        if not self.can_destroy:
            pygame.draw.circle(surface, (100, 100, 100), (self.x + bs, self.y + bs), bs)
        # draw fires
        for fire in self.fires:
            fire.draw(surface)

    def detonate(self, objects, fire_length):
        bs = BLOCK_SIZE

        # these are used to stop the flames from passing through blocks
        up = True
        right = True
        down = True
        left = True

        map_obj = 0

        # gets all the block locations
        for obj in objects:
            if isinstance(obj, map.Map):
                map_obj = obj
                map_objects = obj.get_blocks()


        for i in range(fire_length):

            # up
            temp = (self.x, self.y - (bs * i))
            obj = self.check_empty(temp, map_objects)
            if obj and up:
                self.fires.append(Fire(temp))
                up = False
                if isinstance(obj, crate.Crate):
                    map_obj.destroy_crate(obj)
            else:
                # stop adding fire in this direction
                up = False
            # right
            temp = (self.x + (bs * i), self.y)
            obj = self.check_empty(temp, map_objects)
            if obj and right:
                self.fires.append(Fire(temp))
                right = False
                if isinstance(obj, crate.Crate):
                    map_obj.destroy_crate(obj)
            else:
                # stop adding fire in this direction
                right = False
            # down
            temp = (self.x, self.y + (bs * i))
            obj = self.check_empty(temp, map_objects)
            if obj and down:
                self.fires.append(Fire(temp))
                down = False
                if isinstance(obj, crate.Crate):
                    map_obj.destroy_crate(obj)
            else:
                # stop adding fire in this direction
                down = False
            # left
            temp = (self.x - (bs * i), self.y)
            obj = self.check_empty(temp, map_objects)
            if obj and left:
                self.fires.append(Fire(temp))
                left = False
                if isinstance(obj, crate.Crate):
                    map_obj.destroy_crate(obj)
            else:
                # stop adding fire in this direction
                left = False

    def check_empty(self, dir, map_objects):
        r = pygame.Rect(dir[0], dir[1], BLOCK_SIZE, BLOCK_SIZE)
        for map_obj in map_objects:
            if r.colliderect(map_obj.get_rect()):
                return False
        return map_obj



#######   FIRE   #######
class Fire(main_block.Main_block):
    def __init__(self, dir):
        self.x = (dir[0] // BLOCK_SIZE) * BLOCK_SIZE
        self.y = (dir[1] // BLOCK_SIZE) * BLOCK_SIZE
        super().__init__(self.x, self.y)
        self.can_destroy = False
        self.start = pygame.time.get_ticks()
        self.life_span = 300

    def update(self, objects):
        if pygame.time.get_ticks() - self.start >= self.life_span:
            self.can_destroy = True


    def draw(self, surface):
        pygame.draw.rect(surface, (200, 0, 0), self.rect)
        pygame.draw.rect(surface, (200,200,0), self.rect, 3)

    def get_can_destroy(self):
        return self.can_destroy
