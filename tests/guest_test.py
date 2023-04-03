import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.bar import Bar


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Harry", 150, "Mr Jones")
        self.guest2 = Guest("Albert", 50, "That's Life")
        self.song1 = Song("Mr Jones", "Counting Crows")
        self.song2 = Song("That's Life", "Frank Sinatra")
        self.room = Room(20, 5)

    def test_guest_has_a_name(self):                # THIS RUNS FINE DO NOT TOUCH
        self.assertEqual("Harry", self.guest1.name)

    def test_guest_has_a_wallet(self):              #THIS RUNS FINE DO NOT TOUCH
        self.assertEqual(150,self.guest1.wallet)

    def test_guest_has_a_favourite_song(self):
        self.assertEqual("Mr Jones", self.guest1.favourite_song)    #THIS RUNS FINE DO NOT TOUCH

    def test_fav_song_in_song_list(self):
        self.room.add_song_to_list(self.song1)
        self.room.add_song_to_list(self.song2)
        self.assertEqual("Whoo", self.guest1.cheer_for_song(self.room.songs))