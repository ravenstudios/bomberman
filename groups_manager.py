from constants import *
import sys, pygame, player, map


class Groups_manager:
    def __init__(self):

        self.player_group = pygame.sprite.GroupSingle()
        self.bombs_group = pygame.sprite.Group()
        self.crates_group = pygame.sprite.Group()
        self.border_group = pygame.sprite.Group()
        self.floor_tiles_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()


        self.player = player.Player()
        self.player_group.add(self.player)

        self.collideable_objects = pygame.sprite.Group()
        self.collideable_objects.add(self.crates_group, self.border_group)

        self.drawable_objects = pygame.sprite.Group()

        self.main_group = self.update_main_group()




    def update(self):
        self.main_group = self.update_main_group()
        self.collideable_objects.empty()
        self.collideable_objects.add(self.crates_group, self.border_group)
        self.player_group.update(self)
        self.bombs_group.update(self)
        self.crates_group.update()
        self.border_group.update()
        self.floor_tiles_group.update()
        self.enemy_group.update(self)




    def get_drawing_group(self):
        self.drawable_objects.empty()
        self.drawable_objects.add(
            self.border_group,
            self.floor_tiles_group,
            self.crates_group,
            self.bombs_group,
            self.player_group,
            self.enemy_group
        )
        return self.drawable_objects

    def get_group(self, search):
        return self.main_group[search]

    def get_main_group(self):
        return self.main_group



    def update_main_group(self):
        return {
            "player_group" : self.player_group,
            "bombs_group" : self.bombs_group,
            "crates_group" : self.crates_group,
            "border_group" : self.border_group,
            "floor_tiles_group" : self.floor_tiles_group,
            "collideable_objects" : self.collideable_objects,
            "enemy_group" : self.enemy_group
        }
