from constants import *
import pygame

class Main_entity(pygame.sprite.Sprite):

    """
        # TODO:

    """
    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__()
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.spritesheet = pygame.image.load(SPRITESHEET).convert()
        self.y_sprite_sheet_index = y_sprite_sheet_index

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image = self.get_image_from_sprite_sheet(0, self.y_sprite_sheet_index)
        self.rect = pygame.Rect(self.image.get_rect()).inflate(-10, -10)
        self.rect.topleft = (x, y)

        self.frame = 0
        self.max_frame = (self.spritesheet.get_width() // BLOCK_SIZE) - 1
        self.animation_speed = TICK_RATE / self.max_frame / 100

        self.coords = (self.rect.x // 64, self.rect.y // 64)



    def update(self):

        self.animate()


    def get_image_from_sprite_sheet(self, row, col):
        image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
        image.blit(self.spritesheet, (0, 0), (row, col, BLOCK_SIZE, BLOCK_SIZE))
        #image.set_colorkey()
        return image



    def animate(self):
        self.frame += self.animation_speed

        if self.frame > self.max_frame:
            self.frame = 0

        self.image = self.get_image_from_sprite_sheet(round(self.frame) * BLOCK_SIZE, self.y_sprite_sheet_index)


    def get_coords(self):
        return self.coords
