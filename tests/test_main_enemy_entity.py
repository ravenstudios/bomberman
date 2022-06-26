import unittest, sys, pygame, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import main_enemy_entity

class Test_main_enemy_entity(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()



    def test_is_obj_at_loc_collideable(self):
        self.test_obj = main_enemy_entity.Main_enemy_entity(50, 50, 1)
        self.test_group.add(self.test_obj)
        self.assertNotEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), False)
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.assertEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), True)



if __name__ == '__main__':
    unittest.main()
