class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song



    def buy_drink(self, bar, drink):
        if drink in bar.drinks_list and self.wallet >= bar.drinks_list[drink]:
            bar.tab += bar.drinks_list[drink]

    def cheer_for_song(self, song_list):
        if self.favourite_song in song_list:
            return "Whoo" 
  