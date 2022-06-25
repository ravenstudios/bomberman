import unittest, sys, pygame, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import main_mob_entity,

class Main_mob_entity_tests(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()
        self.test_obj0 = main_mob_entity.Main_mob_entity(50, 50, 1)
        self.test_obj1 = main_mob_entity.Main_mob_entity(50, 50, 1)
        self.test_group.add(self.test_obj0)
        self.test_group.add(self.test_obj1)


    def test_check_collision(self):
        print(self.test_obj0)
        self.assertRaises(ValueError, self.test_obj0.check_collision, self.test_group, "not_vertical")
        self.assertRaises(ValueError, self.test_obj0.check_collision, self.test_group, "not_horizontal")


if __name__ == '__main__':
    unittest.main()
