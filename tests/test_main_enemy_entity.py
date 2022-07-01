import unittest, sys, pygame, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import main_enemy_entity, crate, border_block
from constants import BLOCK_SIZE


class Test_main_enemy_entity(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()


    def test_is_obj_at_loc_collideable(self):
        self.test_obj = main_enemy_entity.Main_enemy_entity(2, 2, 1)
        self.test_group.add(self.test_obj)
        self.assertEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), False, "Returned True that object collieded when should return False")
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.test_group.empty()
        self.test_group.add(self.test_obj)
        self.assertEqual(self.test_obj.is_obj_at_loc_collideable((0, 0), self.test_group), True, "Returned False that object collieded when should return True")


    def test_find_path(self):
        self.maxDiff = None
        # # simple tests
        self.test_obj = main_enemy_entity.Main_enemy_entity(5, 5, 1)
        self.test_group.empty()
        self.test_group.add(border_block.Border_block(1, 1, 0))
        self.test_group.add(border_block.Border_block(2, 2, 0))

        # self.assertIsInstance(self.test_obj.find_path((5, 0), self.test_group), list, "Not an instance of type list")
        # self.assertTrue(len(self.test_obj.find_path((5, 0), self.test_group)) > 0, "Returned list len is not > 0")

        # movment
        # self.test_obj = main_enemy_entity.Main_enemy_entity(5, 5, 1)
        # self.assertEqual(self.test_obj.find_path((5, 0), self.test_group), [(5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)])
        # self.test_obj = main_enemy_entity.Main_enemy_entity(9, 9, 1)
        # self.assertEqual(self.test_obj.find_path((1, 1), self.test_group), [(9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])
        test_list = []
        for i in range(1, 5):
            test_list.append((5 - i, 1))

        self.test_obj = main_enemy_entity.Main_enemy_entity(5, 5, 1)
        self.assertEqual(self.test_obj.find_path((1, 5), self.test_group), test_list)
        # self.assertEqual(self.test_obj.find_path((1, 1), self.test_group), [(9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])
        # advanced test
        # self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        # self.test_group.empty()
        # self.test_group.add(border_block.Border_block(1, 1, 0))
        # self.test_group.add(border_block.Border_block(2, 2, 0))



    def test_move_to_location(self):
        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.test_group.empty()
        self.test_group.add(self.test_obj)
        self.assertIsInstance(self.test_obj.move_to_location((9, 9), self.test_group), pygame.math.Vector2, "Did not return a Vector2")
        self.test_obj = main_enemy_entity.Main_enemy_entity(1, 1, 1)
        self.test_group.empty()
        self.test_group.add(self.test_obj)
        self.assertEqual(self.test_obj.move_to_location((1, 1), self.test_group), f"bomb", "Did not return \"bomb\"")


    def test_search_for_crate(self):

        self.test_obj = main_enemy_entity.Main_enemy_entity(0, 0, 1)
        self.test_group.empty()
        self.test_group.add(crate.Crate(10, 10))
        self.test_group.add(crate.Crate(5, 5))
        self.assertIsInstance(self.test_obj.search_for_crate(self.test_group), pygame.math.Vector2)
        self.assertTrue(len(self.test_obj.search_for_crate(self.test_group)) > 0)


        self.test_group.empty()
        self.test_group.add(crate.Crate(12, 7))
        self.test_group.add(crate.Crate(6, 8))
        self.assertEqual(self.test_obj.search_for_crate(self.test_group), (12 * BLOCK_SIZE, 6 * BLOCK_SIZE))




        # tests to make sure enemy approaches from the correct side
        self.test_obj = main_enemy_entity.Main_enemy_entity(5, 5, 1)
        # right
        self.test_group.empty()
        self.test_group.add(crate.Crate(1, 5))
        self.assertEqual(self.test_obj.search_for_crate(self.test_group), (2 * BLOCK_SIZE, 5 * BLOCK_SIZE))
    # left
        self.test_group.empty()
        self.test_group.add(crate.Crate(8, 5))
        self.assertEqual(self.test_obj.search_for_crate(self.test_group), (7 * BLOCK_SIZE, 5 * BLOCK_SIZE))
    # up
        self.test_group.empty()
        self.test_group.add(crate.Crate(5, 10))
        self.assertEqual(self.test_obj.search_for_crate(self.test_group), (5 * BLOCK_SIZE, 9 * BLOCK_SIZE))
    # down
        self.test_group.empty()
        self.test_group.add(crate.Crate(5, 1))
        self.assertEqual(self.test_obj.search_for_crate(self.test_group), (5 * BLOCK_SIZE, 2 * BLOCK_SIZE))


        # self.assertNotEqual(self.test_obj.search_for_crate(self.test_group), (640, 640))

if __name__ == '__main__':
    unittest.main()
