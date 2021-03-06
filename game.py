# This file contains the functions related to the game
import random


def reset_board():
    """This functions resets the board after every round."""
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]
    return board


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
        player_choice = input(
            f"{player_data['player1'].name}, please choose Heads or Tails. H for Heads, T for Tails: ").upper()
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
    """This function check whether the user's input is valid."""
    valid_input = False
    while not valid_input:
        try:
            # Check whether the user has inputted a number
            user_input = input(f"{player.name}, please choose a square: ")
            board_index = int(user_input) - 1
        except ValueError:
            print("Input is not a number, please try again.")
        else:
            # Check whether square selected doesn't exist in board or is same as player symbols
            if user_input not in board or user_input in player_symbols:
                print("Input doesn't match any available squares, please try again.")
            else:
                # Replace board block with player symbol
                board[board_index] = player.symbol
                valid_input = True


def check_game_state(player, board, turn_number):
    """This function checks for whether there is a win or a draw after every turn."""
    # Check horizontal(3), vertical(3) and diagonal(2)
    if board[0] == board[1] == board[2] == player.symbol or \
            board[3] == board[4] == board[5] == player.symbol or \
            board[6] == board[7] == board[8] == player.symbol or \
            board[0] == board[3] == board[6] == player.symbol or \
            board[1] == board[4] == board[7] == player.symbol or \
            board[2] == board[5] == board[8] == player.symbol or \
            board[0] == board[4] == board[8] == player.symbol or \
            board[2] == board[4] == board[6] == player.symbol:
        player.score += 1
        return "win"
    # Check for draw
    elif turn_number > 9:
        return "draw"
    else:
        return None


def print_scoreboard(player_data):
    """This function prints the user scoreboard after every round."""
    print(f"{player_data['player1'].name} {player_data['player1'].score} - "
          f"{player_data['player2'].score} {player_data['player2'].name}")


def another_round():
    """This function asks the user whether they wish to play another round."""
    valid_input = False
    while not valid_input:
        restart = input('Would you like to play another round? Type "Y" or "N": ').upper()
        if restart == "Y" or restart == "N":
            valid_input = True
            return restart
        else:
            print("Input is invalid, please try again.")
