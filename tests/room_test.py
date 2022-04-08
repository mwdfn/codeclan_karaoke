import unittest

from classes.room import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_info = [
            {
            "room": 1,
            "capacity": 10
            },
            {
            "room": 2,
            "capacity": 10
            },
            {
            "room": 3,
            "capacity": 10
            },
            {
            "room": 4,
            "capacity": 10
            }
        ]

    