# This file contains the Player Item

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.turn_order = None
        self.placements = []
        self.score = 0

    def register_player(number: int):
        """Creates two players, asking for player name and the symbol to be used."""
        player_name = input(f"Player {number}, what is your name? ")
        restricted_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "|", " "]
        valid_symbol = False
        while not valid_symbol:
            player_symbol = input('What symbol would you like to use? "-", "|" and " " are not allowed. ')
            if len(player_symbol) != 1:
                print("Only one character allowed. Please try again.")
            elif player_symbol in restricted_symbols:
                print("This symbol is not allowed. Please try again.")
            else:
                valid_symbol = True
        return Player(player_name, player_symbol)
