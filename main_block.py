from constants import *
import pygame

class Main_block(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, spritesheet_y):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.frame = 0
        self.max_frame = 3
        self.animation_speed = 0.05
        self.spritesheet = pygame.image.load(SPRITESHEET)
        self.spritesheet_y = spritesheet_y
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image = self.get_image_from_sprite_sheet(0, self.spritesheet_y)
        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.topleft = (x, y)


    def update(self):
        self.animate()


    def get_image_from_sprite_sheet(self, row, col):
        image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        image.blit(self.spritesheet, (0, 0), (row, col, BLOCK_SIZE, BLOCK_SIZE))
        #image.set_colorkey()
        return image



    def animate(self):

        self.frame += self.animation_speed

        if self.frame >= self.max_frame:
            self.frame = 0

        self.image = self.get_image_from_sprite_sheet(round(self.frame) * BLOCK_SIZE, self.spritesheet_y)
