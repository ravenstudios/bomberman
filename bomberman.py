
from main_block import *
import map, bomb
class Bomberman(Main_block):

    def __init__(self):
        mul = 0.75
        self.x = self.y = BLOCK_SIZE + BLOCK_SIZE - (BLOCK_SIZE * mul)

        super().__init__(self.x, self.y)
        self.width = self.height = BLOCK_SIZE * mul
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 6
        self.bombs = []
        self.ammo = 100
        self.fire_length = 5

    def update(self, objects):
        self.key_input(objects)

        for b in self.bombs:
            b.update(objects)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
        for b in self.bombs:
            b.draw(surface)


    def key_input(self, objects):
        keys = pygame.key.get_pressed()
        map_objects = 0



        for obj in objects:
            if isinstance(obj, map.Map):
                map_objects = obj.get_blocks()



        if (keys[pygame.K_s] or keys[pygame.K_DOWN]):
            if not self.walk((0, self.speed), map_objects):
                self.rect = self.rect.move(0, self.speed)

        if (keys[pygame.K_w] or keys[pygame.K_UP]):
            if not self.walk((0, -self.speed), map_objects):
                self.rect = self.rect.move(0, -self.speed)

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            if not self.walk((-self.speed, 0), map_objects):
                self.rect = self.rect.move(-self.speed, 0)

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            if not self.walk((self.speed, 0), map_objects):
                self.rect = self.rect.move(self.speed, 0)


    def drop_bomb(self):
        if self.ammo > 0:
            self.bombs.append(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
            self.ammo -= 1
