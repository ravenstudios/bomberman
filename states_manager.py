from constants import *
import sys, pygame, player, map, groups_manager


class States_manager:
    def __init__(self):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[1]

        self.groups_manager = groups_manager.Groups_manager()
        self.map = map.Map(self.groups_manager)





    def draw(self, surface):
        surface.fill((100, 100, 100))#background

        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":
            self.groups_manager.get_drawing_group().draw(surface)


        elif self.state == "paused":
            surface.fill((255, 100, 100))#background


        elif self.state == "dead":
            surface.fill((50, 50, 50))#background

        pygame.display.flip()


    def update(self, surface):
        if self.state == "start":
            pass

        elif self.state == "running":
            self.groups_manager.update()
            self.groups_manager.player_group.update(self.groups_manager)


        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass

    def load_level(self, level):
        self.border_group.empty()
        self.floor_tiles_group.empty()
        self.map.load_level(level, main_group)
        self.collideable_objects.empty()
        self.collideable_objects.add(self.crates_group, self.border_group)



    def events(self, events):

        # print(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                #used to kill outside loop
                if event.key == pygame.K_q:
                    return True
                if event.key == pygame.K_r:
                    # Reset map
                    self.load_level(1)
                if event.key == pygame.K_p:
                    if self.state == "paused":
                        self.state = "running"
                    else:
                        self.state = "paused"

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    if self.state == "start":
                        self.state = "running"
                    # updates the bomb group when you set a bomb
                    if self.state == "running":
                        self.groups_manager.player.set_bomb(self.groups_manager.get_group("bombs_group"))
