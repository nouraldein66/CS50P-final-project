# 5x5 Tic-Tac-Toe Game
####Description:
The game is like any other regular tic-tac-toe game, where you have to achive 3-in-a-row symbols either vertically, horizontally or diagonally,
there are some simple differences that we'll have to mention:
- The board is 5x5 not 3x3
- The player who achieves the highest number of three-in-a-rows will win
- The game ends when there is exactly one place left in the board

Now to talk about how i implemented it:
- I first made a class called Board, which has all the board features
it has 2 parameters: (Board: which is a 2D array that stores the number of each place, places_left: which is the number of places left in the board)
methods: (display: displays the board - state_change: takes a symbol and a number to search for in the board, if it found the number it'll replace it with the symbol and reuturn true,
if not it'll return false so the user should input another value - is_gameOver: checks if the places_left = 1 - check_winner: counts the number of 3 in a row vertically, horizontally and diagonally)

- Then a class called Player which has the player's info: name, symbol and type (either p: for player, c: for cpu)
- lastly is the main function, which handles the gameplay and the program itself, it sets the players' names and symbols and types, starts the game loop, and then when the game is over (places left is 1)
it checks who's the winner and prints that on the screen.
