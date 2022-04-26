# Text-Based Tic Tac Toe
from player import Player
from game import *

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
game_running = True
turn_number = 1

print("Welcome to Tic-Tac-Toe EXTREME!")
# Create & register player details
player_data = {f"player{n}": Player.register_player(n) for n in range(1, 3)}
player_symbols = [player.symbol for player in player_data.values()]

# Determine turn order of players
player_data = turn_order(player_data)

while game_running:
    print("\n" * 1)
    player = current_player(turn_number, player_data)
    print(f"Turn {turn_number}")
    show_board(board)
    input_move(player, board, player_symbols)
    turn_number += 1
    end_result = check_game_state(player, board, turn_number)
    if end_result is None:
        print("No end result")
    elif end_result == "draw":
        print("Game over! It's a draw!")
        game_running = False
    else:
        print(f"{player.name} won!!! Congratulations!")
        game_running = False
    print("\n" * 3)
