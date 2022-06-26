import unittest, sys, pygame, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import main_enemy_entity
from constants import BLOCK_SIZE


class Test_main_enemy_entity(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.test_group.add(self.test_obj)

    def test_is_obj_at_loc_collideable(self):

        self.assertNotEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), False)
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.assertEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), True)


    def test_find_path(self):
        self.test_obj = main_enemy_entity.Main_enemy_entity(9, 9, 1)
        self.test_group.empty()
        self.test_group.add(self.test_obj)
        self.assertIsInstance(self.test_obj.find_path(self.test_group), list)
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.assertIsInstance(self.test_obj.find_path(self.test_group), list)
        self.assertTrue(len(self.test_obj.find_path(self.test_group)) > 0)


    def test_move_to_location(self):
        self.assertIsInstance(self.test_obj.move_to_location((9, 9), self.test_group), pygame.math.Vector2)
        self.test_obj = main_enemy_entity.Main_enemy_entity(1, 1, 1)
        self.test_group.empty()
        self.test_group.add(self.test_obj)
        self.assertEqual(self.test_obj.move_to_location((1, 1), self.test_group), "bomb")


if __name__ == '__main__':
    unittest.main()
