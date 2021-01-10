import main_block, pygame

class Crate(main_block.Main_block):

    def __init__(self, x, y):
        super().__init__(x, y)


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 255), self.rect)
