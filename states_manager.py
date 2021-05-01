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


        self.bomberman_group = pygame.sprite.GroupSingle()
        self.bombs_group = pygame.sprite.Group()
        self.map_group = pygame.sprite.Group()
        self.crates_group = pygame.sprite.Group()
        self.all_group = pygame.sprite.Group()

        self.bm = bomberman.Bomberman()
        self.m = map.Map(self.map_group)
        self.m.add_crates(self.crates_group)
        self.all_group.add(self.map_group)
        self.all_group.add(self.bm)
        self.all_group.add(self.crates_group)
        self.bomberman_group.add(self.bm)




    def events(self, events):

        # print(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    self.running = False

                if event.key == pygame.K_r:
                    # Reset map
                    self.map.reset()

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    # updates the bomb group when you set a bomb

                    self.bm.set_bomb(self.bombs_group)

    def draw(self, surface):
        surface.fill((100, 100, 100))#background
        self.all_group.draw(surface)
        # self.map_group.draw(surface)
        #
        # self.bomberman_group.draw(surface)
        # self.bombs_group.draw(surface)
        # self.crates_group.draw(surface)

        pygame.display.flip()


    def update(self, surface):
        joystick = 0
        self.bomberman_group.update(joystick, self.all_group)
        self.bombs_group.update(self.map_group, self.crates_group, self.bombs_group)
        self.crates_group.update()
