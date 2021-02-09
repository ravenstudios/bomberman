from constants import *
import sys, pygame, bomberman, map

clock = pygame.time.Clock()
screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)
pygame.init()
# pygame.joystick.init()

# joystick_count = pygame.joystick.get_count()

# for i in range(joystick_count):
# if joystick_count:
#
#     joystick = pygame.joystick.Joystick(0)
#     joystick.init()
# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]



bombs_group = 0
bm = 0
map_group = 0
bomberman_group = 0







def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_r:
                    # Reset map
                    map.reset()

            if event.type == pygame.KEYUP:
                if event.key == 32:
                    # updates the bomb group when you set a bomb

                    bm.set_bomb(bombs_group)
                    # print(bombs_groupx)
                    # bombs_group = bombs_groupx
                # keys = pygame.key.get_pressed()
                #
                # if event.key == pygame.K_q:
                #     running = False


        draw()
        update()

    pygame.quit()
    sys.exit()



def draw():
    surface.fill((100, 100, 100))#background
    map_group.draw(surface)


    bomberman_group.draw(surface)
    bombs_group.draw(surface)
    pygame.display.flip()


def update():
    map_group.update()
    joystick = 0
    bomberman_group.update(joystick, map_group, surface)
    bombs_group.update(bombs_group, map_group)


if __name__ == "__main__":
    bombs_group = pygame.sprite.Group()
    bm = bomberman.Bomberman()
    map_group = pygame.sprite.Group()
    map.Map(map_group)
    bomberman_group = pygame.sprite.GroupSingle()
    bomberman_group.add(bm)
    main()
