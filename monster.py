#author Jordan, Dodson, https://github.com/MrBizChicken
from main_block import *
import map

class Monster(Main_block):

    def __init__(self):


        super().__init__(BLOCK_SIZE * 7,  BLOCK_SIZE * 9)

        self.speed = 3


    def update(self, objects):
        self.move_horz(objects)


    def move_vert(self, objects):


        #this function moves vertically and bounces back


        for obj in objects:
            if isinstance(obj, map.Map):
                map_objects = obj.get_blocks()
        if not self.walk((0, self.speed), map_objects):
            self.rect = self.rect.move(0, self.speed)
        else:
            self.speed = -self.speed


    def move_horz(self, objects):


        #this function moves horizontally and bounces back

        for obj in objects:
            if isinstance(obj, map.Map):
                map_objects = obj.get_blocks()
        if not self.walk((self.speed, 0), map_objects):
            self.rect = self.rect.move(self.speed, 0)
        else:
            self.speed = -self.speed


            if self.rect.y >= GAME_HEIGHT + BLOCK_SIZE:

                self.speed = -self.speed
