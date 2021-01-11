from main_block import *

class Bomberman(Main_block):

    def __init__(self):
        self.x, self.y = 0, 0

        super().__init__(self.x, self.y)
    """
    # TODO:
        move bm aka bomberman with W, A, S, D
        and up down left right.
        Dont worry about boundaries because we
        will use unpassable blocks for that.
    """
    def update(self, objects):
        self.key_input()
        # for obj in objects:
        #     self.collide(obj.get_rect())

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] or keys[pygame.K_DOWN] :
            self.rect = self.rect.move(0, self.speed)


        if keys[pygame.K_w] or keys[pygame.K_UP] :
            self.rect = self.rect.move(0, -self.speed)

        if keys[pygame.K_a] or keys[pygame.K_LEFT] :
            self.rect = self.rect.move(-self.speed, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] :
            self.rect = self.rect.move(self.speed, 0)
