import main_block, pygame

class Crate(main_block.Main_block):

    def __init__(self, x, y):
        super().__init__(x, y, 0)
        self.can_remove = False
        self.life_span_after_removal = 300
        self.timer_to_remove_start = 0


    def update(self):

        now = pygame.time.get_ticks()

        if self.can_remove and self.timer_to_remove_start + self.life_span_after_removal < now:
            self.kill()



    def remove(self):
        self.can_remove = True
        self.timer_to_remove_start = pygame.time.get_ticks()
