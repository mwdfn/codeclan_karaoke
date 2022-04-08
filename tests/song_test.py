import unittest

from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_list = [
            {
            "title": "One Beer",
            "artist": "MF DOOM",
            "duration": "04:18"
            },
            {
            "title": "Bohemian Rhapsody",
            "artist": "Queen",
            "duration": "05:54"
            },
            {
            "title": "Drop It Like It's Hot",
            "artist": "Snoop Dogg",
            "duration": "04:26"
            },
            {
            "title": "I Say a Little Prayer",
            "artist": "Aretha Franklin",
            "duration": "03:37"
            }
        ]
    

    def test_song_has_title(self):
        self.assertEqual("One Beer", self.song_list[0]["title"])

    def test_song_has_artist(self):
        self.assertEqual("MF DOOM", self.song_list[0]["artist"])

    def test_song_has_duration(self):
        self.assertEqual("04:18", self.song_list[0]["duration"])

    