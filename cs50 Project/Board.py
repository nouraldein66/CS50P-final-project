class Board:
    def __init__(self):
        self.Board = {0:[1, 2, 3, 4, 5], 1: [6, 7, 8, 9 ,10], 2: [11, 12, 13, 14, 15], 3: [16, 17, 18, 19, 20], 4: [21, 22, 23, 24, 25]}
        self.places_left = 25
    def display(self):
        for key in self.Board:
            for val in self.Board[key]:
                print(f' {val} |', end="")
            print('\n-----------------------\n', end="")

    def state_change(self, symbol, number):
        """
        Searches for the place to put a symbol, if it found that the place is full (there is a symbol in that index)
        it'll return false to make the user input another value

        :param symbol: the symbol that will be put
        :param number: the index to where to put the symbol
        :return: a Boolean value indicating whether it found a place to put the symbol or not
        """
        for key in self.Board:
            for i in range(0, 5):
                if self.Board[key][i] == number:
                    self.Board[key][i] = symbol
                    self.places_left-=1
                    return True
        return False

    def is_gameOver(self):
        return self.places_left == 1

    def check_winner(self):
        """
        counts the number of three-in-a-rows in the board for 'x' and 'o', and returns the symbol with the highest count
        or return 'd' if they're equal indicating it is a draw

        :return: a symbol indicating the player who won, 'x' the winner is the player with 'x' symbol, same with 'o'
        'd' indicates a draw
        """
        countX = 0
        countO = 0
        #horizontal
        for row in self.Board:
            for col in range(0, 3):
                if self.Board[row][col] == self.Board[row][col+1] and self.Board[row][col+1] == self.Board[row][col+2] and self.Board[row][col] == 'x':
                    countX+=1
                elif self.Board[row][col] == self.Board[row][col + 1] and self.Board[row][col + 1] == self.Board[row][
                    col + 2] and self.Board[row][col] == 'o':
                    countO += 1
                
        #vertical
        for col in range(0, 5):
            for row in range(0, 3):
                if self.Board[row][col] == self.Board[row+1][col] and self.Board[row+1][col] == self.Board[row+2][col] and self.Board[row][col] == 'x':
                    countX+=1
                elif self.Board[row][col] == self.Board[row+1][col] and self.Board[row+1][col] == self.Board[row+2][col] and self.Board[row][col] == 'o':
                    countO += 1
                    
        #right diagonal
        for row in range(0, 3):
            for col in range(0, 3):
                if self.Board[row][col] == self.Board[row+1][col+1] and self.Board[row+1][col+1] == self.Board[row+2][col+2] and self.Board[row][col] == 'x':
                    countX+=1
                elif self.Board[row][col] == self.Board[row+1][col+1] and self.Board[row+1][col+1] == self.Board[row+2][col+2] and self.Board[row][col] == 'o':
                    countO+=1

        #left diagonal
        for row in range(0, 3):
            for col in range(4, 1):
                if self.Board[row][col] == self.Board[row+1][col-1] and self.Board[row+1][col-1] == self.Board[row+2][col-2]:
                    if self.Board[row][col] == 'x':
                        countX+=1
                    else:
                        countO+=1

        if countX > countO:
            return 'x'
        elif countO > countX:
            return 'o'
        else:
            return 'd'
