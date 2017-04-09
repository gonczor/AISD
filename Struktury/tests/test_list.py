import unittest

from errors import NotFoundError
from structures.lists import ListHandler


class TestList (unittest.TestCase):
    FIRST_VALUE = 5
    MIDDLE_VALUE = 6
    LAST_VALUE = 1

    def setUp(self):
        ListHandler.add_element(self.FIRST_VALUE)
        ListHandler.add_element(self.MIDDLE_VALUE)
        ListHandler.add_element(self.LAST_VALUE)

    def test_head_gets_deleted(self):
        ListHandler.remove_element(self.FIRST_VALUE)
        self.assertRaises(NotFoundError, ListHandler.find_by_value, self.FIRST_VALUE)

    def test_middle_get_deleted(self):
        ListHandler.remove_element(self.MIDDLE_VALUE)
        self.assertRaises(NotFoundError, ListHandler.find_by_value, self.MIDDLE_VALUE)

    def test_last_get_deleted(self):
        ListHandler.remove_element(self.LAST_VALUE)
        self.assertRaises(NotFoundError, ListHandler.find_by_value, self.LAST_VALUE)

    def tearDown(self):
        ListHandler.clear()
