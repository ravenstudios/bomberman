from constants import *
from main_mob_entity import *
import map, bomb


class Player(Main_mob_entity):

    def __init__(self):
        super().__init__(BLOCK_SIZE, BLOCK_SIZE, 320)
        self.speed = 4
        self.animation_speed = 0.08
        self.fire_length = 3


    def update(self, joystick, collideable_objects, bombs_group):
        self.input(joystick,  bombs_group)
        self.move(collideable_objects)
        self.check_dir()
        self.animate()


    def check_dir(self):
        if self.direction.x > 0:
            self.y_sprite_sheet_index = BLOCK_SIZE * 4;
        if self.direction.x < 0:
            self.y_sprite_sheet_index = BLOCK_SIZE * 5;
        if self.direction.y < 0:
            self.y_sprite_sheet_index = BLOCK_SIZE * 3;
        if self.direction.y > 0:
            self.y_sprite_sheet_index = BLOCK_SIZE * 2;
        if self.direction == [0, 0]:
            self.y_sprite_sheet_index = BLOCK_SIZE * 6;

    def input(self, joystick, bombs_group):
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

        # DOWN
        if (keys[pygame.K_s] or keys[pygame.K_DOWN] or buttons[6]):
            self.direction.y = 1

        # UP
        elif (keys[pygame.K_w] or keys[pygame.K_UP] or buttons[4]):
            self.direction.y = -1
        else:
            self.direction.y = 0

        # LEFT
        if (keys[pygame.K_a] or keys[pygame.K_LEFT] or buttons[7]):
            self.direction.x = -1
        # RIGHT
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT] or buttons[5]):
            self.direction.x = 1
        else:
            self.direction.x = 0

        #SPACE / SET Bomb
        if (keys[pygame.K_SPACE]):
            self.set_bomb(bombs_group)



    def move(self, sprite_group):
        self.rect.x += self.direction.x * self.speed
        self.corner_assist(sprite_group)
        self.check_collision(sprite_group, "horizontal")

        self.rect.y += self.direction.y * self.speed
        self.corner_assist(sprite_group)
        self.check_collision(sprite_group, "vertical")



    def corner_assist(self, sprite_group):
        # if not center on a block move right or left to assist in going down if blocked
        for object_hit in pygame.sprite.spritecollide(self, sprite_group, False):

            if self.rect.center[0] < object_hit.rect.left and self.rect.right > object_hit.rect.left:
                self.rect.x += -self.speed
            if self.rect.center[0] > object_hit.rect.right and self.rect.left < object_hit.rect.right:
                self.rect.x += self.speed
            if self.rect.center[1] < object_hit.rect.top and self.rect.bottom > object_hit.rect.top:
                self.rect.y += -self.speed
            if self.rect.center[1] > object_hit.rect.bottom and self.rect.top < object_hit.rect.bottom:
                self.rect.y += self.speed



    def set_bomb(self, bombs_group):
        bombs_group.add(bomb.Bomb(self.rect.x, self.rect.y, self.fire_length))
