import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bohemian Rhapsody", "Queen", "05:54")
            # {
            # "title": "One Beer",
            # "artist": "MF DOOM",
            # "duration": "04:18"
            # },
            # {
            # "title": "Bohemian Rhapsody",
            # "artist": "Queen",
            # "duration": "05:54"
            # },
            # {
            # "title": "Drop It Like It's Hot",
            # "artist": "Snoop Dogg",
            # "duration": "04:26"
            # },
            # {
            # "title": "I Say a Little Prayer",
            # "artist": "Aretha Franklin",
            # "duration": "03:37"
            # }

    def test_song_has_title(self):
        self.assertEqual("Bohemian Rhapsody", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual("05:54", self.song.duration)

