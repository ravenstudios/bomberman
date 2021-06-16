
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



    def update(self, joystick, all_group, bombs_group):
        self.input(joystick, all_group, bombs_group)
        self.animate()




    def input(self, joystick, all_group, bombs_group):
        # x == 14
        # get the pressed keys on keyboard
        keys = pygame.key.get_pressed()
        # print("keys")
        # print(pygame.K_s)

        # get pressed buttons on joypad
        buttons = []

        if not joystick:
            for i in range(20):
                buttons.append(0)
        else:
            for i in range(joystick.get_numbuttons()):
                buttons.append(joystick.get_button(i))

        # # map_group = map.get_blocks()
        # spritecollide(sprite, group, dokill)

        # DOWN
        if (keys[pygame.K_s] or keys[pygame.K_DOWN] or buttons[6]):
            # move
            self.rect = self.rect.move(0, self.speed)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(0, -self.speed)

            # if not center on a block move right or left to assist in going down if blocked
            for h in hits:
                if self.rect.center[0] < h.rect.left and self.rect.right > h.rect.left:
                    self.rect = self.rect.move(-self.speed, 0)
                if self.rect.center[0] > h.rect.right and self.rect.left < h.rect.right:
                    self.rect = self.rect.move(self.speed, 0)

        # UP
        if (keys[pygame.K_w] or keys[pygame.K_UP] or buttons[4]):
            # move
            self.rect = self.rect.move(0, -self.speed)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(0, self.speed)

            # if not center on a block move right or left to assist in going down if blocked
            for h in hits:
                if self.rect.center[0] < h.rect.left and self.rect.right > h.rect.left:
                    self.rect = self.rect.move(-self.speed, 0)
                if self.rect.center[0] > h.rect.right and self.rect.left < h.rect.right:
                    self.rect = self.rect.move(self.speed, 0)

        # LEFT
        if (keys[pygame.K_a] or keys[pygame.K_LEFT] or buttons[7]):
            # move
            self.rect = self.rect.move(-self.speed, 0)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(self.speed, 0)

            # if not center on a block move right or left to assist in going down if blocked
            for h in hits:
                if self.rect.center[1] < h.rect.top and self.rect.bottom > h.rect.top:
                    self.rect = self.rect.move(0, -self.speed)
                if self.rect.center[1] > h.rect.bottom and self.rect.top < h.rect.bottom:
                    self.rect = self.rect.move(0, self.speed)

        # RIGHT
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT] or buttons[5]):
            # move
            self.rect = self.rect.move(self.speed, 0)
            # gets all sprites that it collided with
            hits = pygame.sprite.spritecollide(self, all_group, False)
            # if we did hit anything move back to make sure were not stuck
            if hits:
                self.rect = self.rect.move(-self.speed, 0)

            # if not center on a block move right or left to assist in going down if blocked
            for h in hits:
                if self.rect.center[1] < h.rect.top and self.rect.bottom > h.rect.top:
                    self.rect = self.rect.move(0, -self.speed)
                if self.rect.center[1] > h.rect.bottom and self.rect.top < h.rect.bottom:
                    self.rect = self.rect.move(0, self.speed)

        # SPACE / SET Bomb
        # if (keys[pygame.K_SPACE]):
        #     self.set_bomb(bombs_group)


    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
        print("bomb set ")
        print(bombs_group)
