import unittest, sys, pygame, os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import main_entity

class Main_entity_tests(unittest.TestCase):

    def setUp(self):
        pygame.init()
        surface = pygame.display.set_mode((100, 100))
        self.test_group = pygame.sprite.Group()
        self.test_obj = main_entity.Main_entity(50, 50, 1)

        self.test_group.add(self.test_obj)


    def test_Main_entity(self):
        self.assertEqual(type(self.test_obj.spritesheet), pygame.Surface)
        # self.assertRaises(ValueError, self.test_obj0.check_collision, self.test_group, "not_vertical")
        # self.assertRaises(ValueError, self.test_obj0.check_collision, self.test_group, "not_horizontal")

    def test_get_image_from_sprite_sheet(self):
        self.assertRaises(ValueError, self.test_obj.get_image_from_sprite_sheet, -1, 1)
        self.assertRaises(ValueError, self.test_obj.get_image_from_sprite_sheet, 1, -1)
        self.assertRaises(ValueError, self.test_obj.get_image_from_sprite_sheet, 1000, 1)
        self.assertRaises(ValueError, self.test_obj.get_image_from_sprite_sheet, 1, 1000)


        self.assertEqual(type(self.test_obj.get_image_from_sprite_sheet(1, 1)), pygame.Surface)


    # def get_image_from_sprite_sheet(self, row, col):
    #     image = pygame.Surface([BLOCK_SIZE, BLOCK_SIZE])
    #     image.blit(self.spritesheet, (0, 0), (row, col, BLOCK_SIZE, BLOCK_SIZE))
    #     #image.set_colorkey()
    #     return image


if __name__ == '__main__':
    unittest.main()
