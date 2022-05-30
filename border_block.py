from main_non_destroyable_block import *

class Border_block(Main_non_destroyable_block):

    def __init__(self, x, y):
        super().__init__(x, y, 0)

    def update(self):
        self.animate()
