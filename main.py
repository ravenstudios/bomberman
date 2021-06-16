from constants import *
import sys, pygame, states_manager
from pygame_tools import make_map





def main():
    sm = states_manager.States_manager()
    clock = pygame.time.Clock()
    screen_size = pygame.FULLSCREEN
    surface = pygame.display.set_mode((0, 0), screen_size)
    pygame.init()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

        clock.tick(TICK_RATE)

        sm.events(pygame.event.get())
        sm.update(surface)
        sm.draw(surface)


    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
