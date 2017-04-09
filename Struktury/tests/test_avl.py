import unittest
from structures.avl import AVLHandler


class AVLTestCase(unittest.TestCase):
    def tearDown(self):
        AVLHandler.clear()

    def test_left_rotation(self):
        """Test that after inserting 1, 2, 3 there is left rotation: height should be 2"""
        values = [1, 2, 3]
        for v in values:
            AVLHandler.add_element(v)

        self.assertEqual(AVLHandler.get_height(), 2)

    def test_right_rotation(self):
        """Test that after inserting sequence 3, 2, 1 height is 2"""
        values = [3, 2, 1]
        for v in values:
            AVLHandler.add_element(v)

        self.assertEqual(AVLHandler.get_height(), 2)
