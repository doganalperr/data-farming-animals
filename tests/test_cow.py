import unittest
from farm.cow import Cow


class TestCow(unittest.TestCase):
    def setUp(self):
        self.cow = Cow()

    def test_initialize_sets_energy_to_zero(self):
        self.assertEqual(self.cow.energy, 0)

    def test_initialize_sets_milk_to_zero(self):
        self.assertEqual(self.cow.milk, 0)

    def test_feed_adds_energy(self):
        self.cow.feed()
        self.assertEqual(self.cow.energy, 1)

    def test_feed_adds_milk(self):
        self.cow.feed()
        self.assertEqual(self.cow.milk, 2)

    def test_feed_extends_method(self):
        self.cow.feed()
        self.assertGreater(self.cow.energy, 0)
        self.assertGreater(self.cow.milk, 0)

    def test_talk_returns_correct_sound(self):
        self.assertEqual(self.cow.talk(), "moo")
