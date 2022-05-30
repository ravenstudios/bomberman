from constants import *
import sys, pygame, states_manager






def main():
    sm = states_manager.States_manager()
    clock = pygame.time.Clock()
    screen_size = pygame.FULLSCREEN
    surface = pygame.display.set_mode((0, 0), screen_size)
    pygame.init()

    running = True

    while running:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

        clock.tick(TICK_RATE)

        sm.events(events)
        sm.update(surface)
        sm.draw(surface)


    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
