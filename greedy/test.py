import unittest

from main import Load, Container, OverloadError


class TestGreedy(unittest.TestCase):
    def setUp(self):
        self.MAX_WEIGHT = 5
        self.load = Load(self.MAX_WEIGHT)

    def test_add_raises_overload(self):
        too_heavy_element = Container(weight=self.MAX_WEIGHT+1, price=5)

        with self.assertRaises(OverloadError):
            self.load.add(too_heavy_element)

        self.assertEqual(self.load.load, [])

    def test_add_adds_elements(self):
        c1 = Container(weight=1, price=1)
        c2 = Container(weight=2, price=3)
        c3 = Container(weight=2, price=4)
        containers = [
            c3, c2, c1
        ]

        for container in containers:
            self.load.add(container)

        self.assertEqual(
            self.load.load,
            [c3, c2, c1]
        )
