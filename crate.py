import main_block, pygame

class Crate(main_block.Main_block):

    def __init__(self, x, y):
        super().__init__(x, y)


    def draw(self, surface):
        pygame.draw.rect(surface, (150,75,0), self.rect)
        pygame.draw.rect(surface, (50,10,75), self.rect, 3)
