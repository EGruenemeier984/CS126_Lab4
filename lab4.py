# imports the random library from python
import random
# These are global variables for the squares that will appear to the user
X = "\u25A1"
Y = "\u25A0"
Z = [X, Y]
maps = {X:Y, Y:X}
# The main funct calls the game function with the creategrid function as the argument.
def main():
    game(createGrid())
# This function creates a multi dimensional list of unicode squares randomly and formats them into a five by five grid.
def createGrid():
    board = []
    for rows in range(0, 5):
        row = []
        for pos in range(0, 5):
            randomZ = random.choice(Z)
            row.append(randomZ)
        board.append(row)
    for rows in board:
        game_board = " ".join(rows)
        print(game_board)
    return board
# The game funct starts the user interaction and counts the number of moves the user takes. 
def game(board):
    moves = 0
    while not is_solved(board):
        row = int(input("Please select a row (0-4): ")) 
        col = int(input("Please select a column (0-4): ")) 
        touch(board, row, col)
        moves += 1
        print(f"Total Moves: {moves}")
        for rows in board:
            print(" ".join(rows))
    print("YOU WIN!!!")
# This funct takes in the game board and the rows and col of the board and uses a dictionary to map the unicode in the list.
# Uses conditionals to account for speacial cases (edges of board)
def touch(board, row, col):
    if row == 0 and col == 0:
        board[row][col] = maps[board[row][col]]
        board[row][col + 1] = maps[board[row][col + 1]]
        board[row + 1][col] = maps[board[row + 1][col]]
    elif row == 0 and col == 4:
        board[row][col] = maps[board[row][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row + 1][col] = maps[board[row + 1][col]]
    elif row == 4 and col == 0:
        board[row][col] = maps[board[row][col]]
        board[row][col + 1] = maps[board[row][col + 1]]
        board[row - 1][col] = maps[board[row - 1][col]]
    elif row == 4 and col == 4:
        board[row][col] = maps[board[row][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row - 1][col] = maps[board[row - 1][col]]
    elif row == 4:
        board[row][col] = maps[board[row][col]]
        board[row - 1][col] = maps[board[row - 1][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row][col + 1] = maps[board[row][col + 1]]
    elif row == 0:
        board[row][col] = maps[board[row][col]]
        board[row + 1][col] = maps[board[row + 1][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row][col + 1] = maps[board[row][col + 1]]
    elif col == 4:
        board[row][col] = maps[board[row][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row + 1][col] = maps[board[row + 1][col]]
        board[row - 1][col] = maps[board[row - 1][col]]
    elif col == 0:
        board[row][col] = maps[board[row][col]]
        board[row][col + 1] = maps[board[row][col + 1]]
        board[row + 1][col] = maps[board[row + 1][col]]
        board[row - 1][col] = maps[board[row - 1][col]]
    else:
        board[row][col] = maps[board[row][col]]
        board[row][col - 1] = maps[board[row][col - 1]]
        board[row][col + 1] = maps[board[row][col + 1]]
        board[row + 1][col] = maps[board[row + 1][col]]
        board[row - 1][col] = maps[board[row - 1][col]]

# This function is to check the board to make sure it is not solved
def is_solved(array):
    if array == [[Y, Y, Y, Y, Y],
                [Y, Y, Y, Y, Y],
                [Y, Y, Y, Y, Y],
                [Y, Y, Y, Y, Y],
                [Y, Y, Y, Y, Y]]:
        return True
    elif array == [[X, X, X, X, X],
                    [X, X, X, X, X],
                    [X, X, X, X, X],
                    [X, X, X, X, X],
                    [X, X, X, X, X]]:
        return False
    else: 
        return None
# calls the main funct
main()