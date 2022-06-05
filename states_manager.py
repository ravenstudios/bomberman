from constants import *
import sys, pygame, player, map


class States_manager:
    def __init__(self):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[1]

        self.player_group = pygame.sprite.GroupSingle()
        self.bombs_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.crates_group = pygame.sprite.Group()
        self.border_group = pygame.sprite.Group()
        # self.all_group = pygame.sprite.Group()
        self.floor_tiles_group = pygame.sprite.Group()





        self.player = player.Player()
        self.map = map.Map(self.border_group, self.floor_tiles_group)
        # self.map.add_crates(self.crates_group)
        # self.all_group.add(self.map_group)
        # self.all_group.add(self.border_group)
        # self.all_group.add(self.crates_group)
        self.player_group.add(self.player)

        self.collideable_objects = pygame.sprite.Group()
        self.collideable_objects.add(self.crates_group, self.border_group)



    def events(self, events):

        # print(events)
        for event in events:
            # if event.type == pygame.QUIT:
            #     self.running = False

            #Keyboard
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
                        self.player.set_bomb(self.bombs_group)

    def draw(self, surface):
        surface.fill((100, 100, 100))#background

        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":

            self.border_group.draw(surface)
            self.floor_tiles_group.draw(surface)
            self.crates_group.draw(surface)
            self.bombs_group.draw(surface)
            self.player_group.draw(surface)

        elif self.state == "paused":
            surface.fill((255, 100, 100))#background


        elif self.state == "dead":
            surface.fill((50, 50, 50))#background

        pygame.display.flip()


    def update(self, surface):
        joystick = 0
        if self.state == "start":
            pass
        elif self.state == "running":
            self.player_group.update(joystick, self.collideable_objects, self.bombs_group)
            self.bombs_group.update(self.map_group, self.crates_group, self.bombs_group)
            self.crates_group.update()
            self.border_group.update()
            self.floor_tiles_group.update()

        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass

    def load_level(self, level):
        self.border_group.empty()
        self.floor_tiles_group.empty()
        self.map.load_level(level, self.border_group, self.floor_tiles_group)
        self.collideable_objects.empty()
        self.collideable_objects.add(self.crates_group, self.border_group)
