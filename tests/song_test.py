import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Mr Jones", "Counting Crows")
       


    def test_song_has_a_title(self):
        self.assertEqual("Mr Jones", self.song.title)

    def test_song_has_an_artist(self):
        self.assertEqual("Counting Crows", self.song.artist)

   
        
  