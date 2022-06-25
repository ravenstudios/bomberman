import pygame
from constants import *



# def log(info, x = 10, y = 10):
#     font = pygame.font.Font(None, 90)
#     display_surface = pygame.display.get_surface()
#     debug_surface = font.render(str(info), True, (255, 255, 255))
#     debug_rect = debug_surface.get_rect(topleft = (x, y))
#     pygame.draw.rect(display_surface, (0, 0, 0), debug_rect)
#     display_surface.blit(debug_surface, debug_rect)
#
class Debug_window:
    def __init__(self, x = 10, y = 10):
        self.font = pygame.font.Font(None, 30)

        self.display_data = "DEBUG WINDOWS BITCH"
# pygame.init()


    def log(self, input):
        self.display_data += str(input + "\n")

    def draw(self, surface):
        debug_rect = pygame.rect.Rect(0, 0, surface.get_width(), 64)
        w = surface.get_width()
        h = surface.get_height()
        alpha_surface = pygame.Surface((w, 64), pygame.SRCALPHA)
        alpha_surface.fill((128, 128, 128, 200))
        surface.blit(alpha_surface, debug_rect)
        self.degbug_surface = self.font.render(self.display_data, True, (255, 255, 255))
        surface.blit(self.degbug_surface, debug_rect)
