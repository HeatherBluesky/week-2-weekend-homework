import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.bar import Bar

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(20, 5)
        self.room2 = Room(15, 7)
        self.guest1 = Guest("Harry", 150, "Favourite_song")
        self.guest2 = Guest("Albert", 50, "Favourite_song")
        self.song1 = Song("Mr Jones", "Counting Crows")
        self.song2 = Song("That's Life", "Frank Sinatra")
        self.bar = Bar()
       
       
    def test_room_has_a_fee(self):
        self.assertEqual(20, self.room1.fee)

    def test_room_has_a_capacity(self):
        self.assertEqual(5, self.room1.capacity)

    
    # def test_room_can_add_guest(self):
    #     self.room.check_in(self.guest1, self.bar)
    #     self.room.check_in(self.guest2, self.bar)
    #     self.assertEqual(["Harry", "Albert"], self.guest1, self.guest2 )
    
   
    # def test_room_can_remove_guest(self):
    #      self.check_out(self.guest1)
    #      self.assertEqual(["Albert"], self.guest2)

        