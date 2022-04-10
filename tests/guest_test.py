import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bob", 100)

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest_1.guest_name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.guest_money)
