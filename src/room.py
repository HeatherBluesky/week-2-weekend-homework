class Room:
    def __init__(self, fee, capacity):
        self.songs =[]
        self.fee = fee 
        self.capacity = capacity
        self.guests = []
        self.total_guest_money = 0
        self.guest_money = {}


    # def check_in(self, guest, bar):
    #     if len(self.guests) < self.capacity and guest.wallet >= self.fee:
    #         self.guests.append(guest.name)
    #         self.guest_money[guest.name] = guest.wallet 
    #         self.total_guest_money += guest.wallet 
    #         bar.tab += self.fee  
    #     return "Fully Booked"
    
    # def check_out(self, guest):
    #     self.guests.remove(guest.name)
    #     del self.guest_money[guest.name]
    #     self.total_guest_money -= guest.wallet 
    
    def add_song_to_list(self, song):
        self.songs.append(song.title)  