# This file contains the functions related to the game
import random


def show_board(board):
    """Prints the current state of the tic-tac-toe board."""
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def turn_order(player_data):
    """Lets player 1 choose heads or tails to determine turn order."""
    # Player 1 choose heads or tails
    valid_ht = False
    while not valid_ht:
        player_choice = input(f"{player_data['player1'].name}, please choose Heads or Tails. H for Heads, T for Tails: ").upper()
        if player_choice == "H" or player_choice == "T":
            valid_ht = True
        else:
            print("Invalid choice, please try again.")
    # Flips coin
    coin = random.choice(["H", "T"])
    # If player choice matches
    if player_choice == coin:
        player_data['player1'].turn_order = 1
        player_data['player2'].turn_order = 0
        print(f"The coin shows {coin}, {player_data['player1'].name} starts first.")
    else:
        player_data['player1'].turn_order = 0
        player_data['player2'].turn_order = 1
        print(f"The coin shows {coin}, {player_data['player2'].name} starts first.")
    return player_data


def current_player(turn_number, player_data):
    """This functions determines which player is playing this turn based on the turn number"""
    for player in player_data.values():
        if turn_number % 2 == player.turn_order:
            return player


def input_move(player, board, player_symbols):
    valid_input = False
    while not valid_input:
        try:
            user_input = input(f"{player.name}, please choose a square.")
            board_index = int(user_input) - 1
        except ValueError:
            print("Input is not a number, please try again.")
        else:
            # Check whether square selected doesn't exist in board or is same as player symbols
            if user_input not in board or user_input in player_symbols:
                print("Input doesn't match any available squares, please try again.")
            else:
                board[board_index] = player.symbol
                valid_input = True


def check_game_state(player, board, turn_number):
    # Check for win
    # Check horizontal
    if board[0] == board[1] == board[2] == player.symbol:
        return "win"
    elif board[3] == board[4] == board[5] == player.symbol:
        return "win"
    elif board[6] == board[7] == board[8] == player.symbol:
        return "win"
    # Check vertical
    elif board[0] == board[3] == board[6] == player.symbol:
        return "win"
    elif board[1] == board[4] == board[7] == player.symbol:
        return "win"
    elif board[2] == board[5] == board[8] == player.symbol:
        return "win"
    # Check diagonal
    elif board[0] == board[4] == board[8] == player.symbol:
        return "win"
    elif board[2] == board[4] == board[6] == player.symbol:
        return "win"
    # Check for draw
    elif turn_number > 9:
        return "draw"
    else:
        return None

