from constants import *
import sys, pygame, states_manager






def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen_size = pygame.FULLSCREEN
    print(screen_size)
    # screen_size = [ROWS * BLOCK_SIZE, COLS * BLOCK_SIZE]
    # surface = pygame.display.set_mode((0, 0), screen_size)
    surface = pygame.display.set_mode((COLS * BLOCK_SIZE, ROWS * BLOCK_SIZE))
    sm = states_manager.States_manager()
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
