from constants import *
from main_entity import *



class Main_mob_entity(Main_entity):

    def __init__(self, x, y, y_sprite_sheet_index):
        super().__init__(x, y, y_sprite_sheet_index)
        self.direction = pygame.math.Vector2()



    def check_collision(self, sprite_group, dir):

        if dir == "horizontal":
            for sprite in sprite_group:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                        return sprite
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                        return sprite

        elif dir == "vertical":
            for sprite in sprite_group:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        return sprite
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        return sprite
                        self.rect.top = sprite.rect.bottom


        else:
            raise ValueError("Must use \"horizontal\" or \"vertical\"")
