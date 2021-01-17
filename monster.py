from main_block import *

class Monster(Main_block):

    def __init__(self):


        super().__init__(BLOCK_SIZE * 8,  BLOCK_SIZE * 9)

        self.speed = -5


    def update(self, objects):
        self.move_vert()


    def move_vert(self):

            self.rect = self.rect.move(0, self.speed)

            if self.rect.y <= 0:
                self.speed = -self.speed

            if self.rect.y >= BLOCK_SIZE * 8 :
                self.speed = -self.speed
