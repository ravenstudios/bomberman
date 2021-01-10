from main_block import *

class Border_block(Main_block):

    def __init__(self, x, y):
        super().__init__(x, y)


    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (0, 100, 0), self.rect, 3)
