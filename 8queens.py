import random

# REPLACE THIS FUNCTION with one to find all possible ways to put 8 queens on a board so that they can't take each other!
# NOTE: as I place the queens, I check to see if it's a valid board with this queen placed. The code to do that might be helpful for what you're trying to do!
def randomlyPlace8Queens():
    
    # make an empty board
    board = []
    legal = True
    queenPositions = []
    
    for row in range(8):
        board.append(["_", "_", "_", "_", "_", "_", "_", "_"])

    # place random queens until we've placed 8
    # if we try to place a queen on top of another queen, try a different square
    placed = 0

    while placed < 8:
        row = random.randint(0, 7)
        col = random.randint(0, 7)

        # if it's empty, place the queen
        if board[row][col] == "_":
            board[row][col] = "Q"
            placed += 1
            
            # check if it can take any queens
            for queen in queenPositions:
                if isPossible(row, col, queen[0], queen[1]):
                    legal = False
            
            queenPositions.append([row, col])
    
    # return the board
    return [board, legal]


# HELPER FUNCTION to tell if a row/col is accessible by a queen at queenRow/queenCol
def isPossible(queenRow, queenCol, row, col):

    # a queen can't take itself
    if queenRow == row and queenCol == col:
        return False
    
    # check row
    if row == queenRow:
        return True
    
    # check column
    if col == queenCol:
        return True
    
    # check diagonal
    if abs(queenRow - row) == abs(queenCol - col):
        return True
    
# UTILITY FUNCTION to print the board nicely
def printBoard(board):
    for row in range(8):
        for col in range(8):
            print(board[row][col], end = " ")
        print()


# RUN THE PROGRAM UNTIL WE GET LUCKY
success = False
while not success:
    testBoard = randomlyPlace8Queens()

    legal = testBoard[1]
    testBoard = testBoard[0]

    printBoard(testBoard)

    if legal:
        print("What are the odds! We randomly generated one that works!")
        success = True
    else:
        print("As expected, some of the queens can take each other.")
    print()

