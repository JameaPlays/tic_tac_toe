# Text-Based Tic Tac Toe
from player import Player
from game import *

print("Welcome to Tic-Tac-Toe EXTREME!")
# Create & register player details
player_data = {f"player{n}": Player.register_player(n) for n in range(1, 3)}
player_symbols = [player.symbol for player in player_data.values()]

game_running = True
board = []

while game_running:
    # Reset the board and turn number after every round
    board = reset_board()
    turn_number = 1

    # Determine turn order of players
    player_data = turn_order(player_data)

    new_turn = True
    while new_turn:
        player = current_player(turn_number, player_data)
        print(f"Turn {turn_number}")
        show_board(board)
        input_move(player, board, player_symbols)

        # Checks for win or draw conditions
        end_result = check_game_state(player, board, turn_number)
        if end_result is None:
            pass
        else:
            print("\n" * 3)
            show_board(board)
            if end_result == "draw":
                print("Game over! It's a draw!")
            else:
                print(f"{player.name} won!!! Congratulations!")
            print_scoreboard(player_data)
            new_turn = False

        # Increase turn number after a turn has ended
        turn_number += 1
        print("\n" * 3)

    # Asks player if they wish to play another round
    restart = another_round()
    if restart == "N":
        game_running = False
