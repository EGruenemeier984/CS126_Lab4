import random

X = "\u25A1" #white square
Y = "\u25A0" #black square
Z = [X, Y]
# map white square to black square and black square to white square 
maps = {X:Y, Y:X}


def main():
        playGame()

def createGrid():
	board = []
	for rows in range(0, 5):
		row = []
		for pos in range(0, 5):
			randomZ = random.choice(Z)
			row.append(randomZ)
		board.append(row)
	for rows in board:
		print(" ".join(rows))
	return board


def playGame():
        gameBoard = createGrid()
        moves = 0
        while gameBoard != [[Y, Y, Y, Y, Y],
                            [Y, Y, Y, Y, Y],
                            [Y, Y, Y, Y, Y],
                            [Y, Y, Y, Y, Y],
                            [Y, Y, Y, Y, Y]
                            ]:
                rowSelect = int(input("Please select a row: ")) - 1
                colSelect = int(input("Please select a column: ")) - 1
                if rowSelect == 0 and colSelect == 0:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                elif rowSelect == 0 and colSelect == 4:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                elif rowSelect == 4 and colSelect == 0:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                elif rowSelect == 4 and colSelect == 4:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                elif rowSelect == 4:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                elif rowSelect == 0:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                elif colSelect == 4:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                elif colSelect == 0:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                else:
                        gameBoard[rowSelect][colSelect] = maps[gameBoard[rowSelect][colSelect]]
                        gameBoard[rowSelect][colSelect - 1] = maps[gameBoard[rowSelect][colSelect - 1]]
                        gameBoard[rowSelect][colSelect + 1] = maps[gameBoard[rowSelect][colSelect + 1]]
                        gameBoard[rowSelect + 1][colSelect] = maps[gameBoard[rowSelect + 1][colSelect]]
                        gameBoard[rowSelect - 1][colSelect] = maps[gameBoard[rowSelect - 1][colSelect]]
                moves += 1
                print(f"Total Moves: {moves}")
                for rows in gameBoard:
                        print(" ".join(rows))
        print("YOU WIN!!!")


                
                
        
    
