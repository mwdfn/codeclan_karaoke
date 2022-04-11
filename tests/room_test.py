import unittest

from classes.room import *
from classes.guest import *
from classes.song import *
class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_number = Room(1, 10)
        self.guest_list = []
        self.song_list = []
        
        self.guest_name = ("Bob")
        self.song_name = ("Bohemian Rhapsody")

        #"Bob", "Linda", "Tina", "Gene", "Louise"

    def test_room_has_number(self):
        self.assertEqual(1, self.room_number.room_number)

    def test_guest_list_len(self):
        self.assertEqual(0, Room.check_guest_list_len(self))

    def test_song_list_len(self):
        self.assertEqual(0, Room.check_song_list_len(self))

    def test_guest_added_to_room_list(self):
        Room.add_guest_to_list(self, self.guest_name)
        self.assertEqual(1, Room.check_guest_list_len(self))

    def test_add_song_to_room(self):
        Room.add_song_to_list(self, self.song_name)
        self.assertEqual(1, Room.check_song_list_len(self))

    def test_is_room_capacity_full(self):
        Room.check_room_capacity(self, 10)
        self.assertEqual("Sorry, all rooms are full", self.room_capacity)

    