
from main_block import *
import map, bomb
class Bomberman(Main_block):

    def __init__(self):
        mul = 0.50
        self.x, self.y = BLOCK_SIZE * mul, BLOCK_SIZE  * mul
        super().__init__(self.x + (BLOCK_SIZE - (BLOCK_SIZE * mul)), self.y + (BLOCK_SIZE - (BLOCK_SIZE * mul)), 320)
        self.width = BLOCK_SIZE * mul
        self.height = BLOCK_SIZE * mul
        self.speed = 4
        self.animation_speed = self.speed * 0.01 * 2
        self.fire_length = 3


    def update(self, joystick, map):
        self.input(joystick, map)
        self.animate()



    def input(self, joystick, map):
        # x == 14
        # get the pressed keys on keyboard
        keys = pygame.key.get_pressed()

        # get pressed buttons on joypad
        buttons = []

        if not joystick:
            for i in range(20):
                buttons.append(0)
        else:
            for i in range(joystick.get_numbuttons()):
                buttons.append(joystick.get_button(i))

        map_objects = map.get_blocks()


        # DOWN
        if (keys[pygame.K_s] or keys[pygame.K_DOWN] or buttons[6]):
            self.rect = self.rect.move(0, self.speed)
            if pygame.sprite.spritecollide(self, map_objects, False):
                self.rect = self.rect.move(0, -self.speed)

        # UP
        if (keys[pygame.K_w] or keys[pygame.K_UP] or buttons[4]):
            self.rect = self.rect.move(0, -self.speed)
            if pygame.sprite.spritecollide(self, map_objects, False):
                self.rect = self.rect.move(0, self.speed)

        # LEFT
        if (keys[pygame.K_a] or keys[pygame.K_LEFT] or buttons[7]):
            self.rect = self.rect.move(-self.speed, 0)
            if pygame.sprite.spritecollide(self, map_objects, False):
                self.rect = self.rect.move(self.speed, 0)

        # RIGHT
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT] or buttons[5]):
            self.rect = self.rect.move(self.speed, 0)
            if pygame.sprite.spritecollide(self, map_objects, False):
                self.rect = self.rect.move(-self.speed, 0)

        # SPACE and "X" button 14
        if keys[pygame.K_SPACE] or buttons[14]:
            self.set_bomb()


    def set_bomb(self):
        print("bomb")
