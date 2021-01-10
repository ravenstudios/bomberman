from constants import *
import pygame, crate, bomberman


objects = []

crate = crate.Crate(100, 100)
bm = bomberman.Bomberman()

objects.append(crate)
objects.append(bm)

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

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
