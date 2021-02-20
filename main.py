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
crates_group = 0
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
                if event.key == 32:#SPACE
                    # updates the bomb group when you set a bomb

                    bm.set_bomb(bombs_group)

        draw()
        update()

    pygame.quit()
    sys.exit()



def draw():
    surface.fill((100, 100, 100))#background
    map_group.draw(surface)

    bomberman_group.draw(surface)
    bombs_group.draw(surface)
    crates_group.draw(surface)

    pygame.display.flip()


def update():
    # map_group.update()
    joystick = 0
    bomberman_group.update(joystick, map_group, crates_group, surface)
    bombs_group.update(map_group, crates_group, bombs_group)
    crates_group.update()


if __name__ == "__main__":

    bomberman_group = pygame.sprite.GroupSingle()
    bombs_group = pygame.sprite.Group()
    map_group = pygame.sprite.Group()
    crates_group = pygame.sprite.Group()


    bm = bomberman.Bomberman()
    m = map.Map(map_group)
    m.add_crates(crates_group)


    bomberman_group.add(bm)







    main()



# width = 20
# height = 10
# gap = 2
#
# rows = 5
# cols = 5
#
# for r in rows:
#
#     for c in cols:
#         group.add(new brick(r * width + gap, c * height  + gap))
