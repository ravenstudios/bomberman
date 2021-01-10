
import main_block

class Bomberman(main_block.Main_block):

    def __init__(self):
        self.x, self.y = 300, 300
        super().__init__(self.x, self.y)
    """
    # TODO:
        move bm aka bomberman with W, A, S, D
        and up down left right.
        Dont worry about boundaries because we
        will use unpassable blocks for that.
    """
    def update(self, objects):
        pass
