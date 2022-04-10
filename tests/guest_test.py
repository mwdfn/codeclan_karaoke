import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Bob")

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest_1.guest_name)


