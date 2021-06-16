from constants import *
import sys, pygame, bomberman, map


# pygame.joystick.init()

# joystick_count = pygame.joystick.get_count()

# for i in range(joystick_count):
# if joystick_count:
#
#     joystick = pygame.joystick.Joystick(0)
#     joystick.init()
# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
class States_manager:
    def __init__(self):
        self.running = True
        self.states = ["start", "running", "paused", "dead"]
        self.state = self.states[0]

        self.bomberman_group = pygame.sprite.GroupSingle()
        self.bombs_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.crates_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()

        self.bm = bomberman.Bomberman()
        self.m = map.Map(self.map_group)
        self.m.add_crates(self.crates_group)
        self.all_group.add(self.map_group)
        # self.all_group.add(self.bm)
        self.all_group.add(self.crates_group)
        self.bomberman_group.add(self.bm)




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
                    self.map.reset()

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
                        self.bm.set_bomb(self.bombs_group)

    def draw(self, surface):
        surface.fill((100, 100, 100))#background

        if self.state == "start":
            surface.fill((100, 100, 255))#background

        elif self.state == "running":
            self.bomberman_group.draw(surface)
            self.all_group.draw(surface)
            self.bombs_group.draw(surface)

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
            self.bomberman_group.update(joystick, self.all_group, self.bombs_group)
            self.bombs_group.update(self.map_group, self.crates_group, self.bombs_group)
            self.crates_group.update()
        elif self.state == "paused":
            pass
        elif self.state == "dead":
            pass
