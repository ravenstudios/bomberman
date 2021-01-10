from constants import *
import pygame

class Main_block:

    """
        # TODO:

    """
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 1

    def update(self, objects):
        self.rect = self.rect.move(self.speed, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def get_rect(self):
        return self.rect
