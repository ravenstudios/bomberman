from constants import *
import pygame, bomberman, map


objects = []


bm = bomberman.Bomberman()
map = map.Map()


objects.append(map)
objects.append(bm)


clock = pygame.time.Clock()
surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    bm.drop_bomb()


            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((0, 0, 0))#background


    for obj in objects:
        obj.draw(surface)

    pygame.display.flip()



def update():

    for obj in objects:
        obj.update(objects)



if __name__ == "__main__":
    main()
