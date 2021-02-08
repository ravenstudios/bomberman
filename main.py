from constants import *
import pygame, bomberman, map

clock = pygame.time.Clock()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
# pygame.joystick.init()

# joystick_count = pygame.joystick.get_count()

# for i in range(joystick_count):
# if joystick_count:
#
#     joystick = pygame.joystick.Joystick(0)
#     joystick.init()
# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]




bm = bomberman.Bomberman()
map = map.Map()

bmg = pygame.sprite.GroupSingle()
bmg.add(bm)






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


        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((100, 100, 100))#background
    map.draw(surface)
    bmg.draw(surface)
    pygame.display.flip()


def update():
    map.update()
    joystick = 0
    bmg.update(joystick, map)


if __name__ == "__main__":
    main()
