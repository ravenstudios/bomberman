from constants import *
import pygame

class Main_block:

    """
        # TODO:

    """
    def __init__(self, x, y):

        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.rect = pygame.Rect(x, y, self.width, self.height)


    def update(self, objects):
        pass


    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)


    def get_rect(self):
        return self.rect


    def walk(self, dir, map_objects):
        r = self.rect.move(dir)
        for map_obj in map_objects:
            if r.colliderect(map_obj.get_rect()):
                
                return True
        return False
