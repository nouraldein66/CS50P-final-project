from Player import Player
from Board import Board
import random


def main():
    print("Welcome to 5x5 tic-tac-toe game, 5x5 tic tac toe is like any regular tic tac toe,\nbut you don't just win by one 3 in a row, rather the player with the highest number of 3 in a rows will win\n\nA 3 in a row in horizontal, vertical or diagonal are all accepted")

    #setting name and symbol for player 1
    name = input("To start the game, please enter your name: ")
    while True:
        symbol = input("please choose a symbol: 'x' or 'o'")
        if symbol.lower() == 'x' or symbol.lower() == 'o':
            break
    player1 = Player('p', name, symbol)

    #setting name and symbol for player 2
    while True:
        choice = input("Press (y) to play with another player, or (n) to play with the computer")
        if choice == 'y' or choice == 'Y':
            name = input("Player 2, plesae enter your name: ")
            if player1.symbol == 'x':
                player2 = Player('p', name, 'o')
            else:
                player2 = Player('p', name, 'x')
            break
        elif choice == 'n' or choice == 'N':
            if player1.symbol == 'x':
                player2 = Player('c', 'CPU', 'o')
            else:
                player2 = Player('c', 'CPU', 'x')
            break

    #game loop
    board = Board()
    player1_turn = True
    while not board.is_gameOver():
        board.display()
        if player1_turn:
            number = int(input(f"{player1.name}'s turn, please enter a number: "))
            while not board.state_change(player1.symbol, number):
                number = int(input("invalid input, please enter another value: "))
        else:
            if player2.type == 'c':
                while True:
                    if board.state_change(player2.symbol, random.randint(1, 25)):
                        break
            else:
                number = int(input(f"{player2.name}'s turn, please enter a value: "))
                while not board.state_change(player2.symbol, number):
                    number = int(input("invalid input, please enter another value: "))

        player1_turn = not player1_turn

    #Game ends, checking winning condition
    condition = board.check_winner()
    if condition == player1.symbol:
        print(f"{player1.name} won! congratulations!!")
    elif condition == player2.symbol:
        print(f"{player2.name} won! congratulations!!")
    else:
        print("Draw!")

main()