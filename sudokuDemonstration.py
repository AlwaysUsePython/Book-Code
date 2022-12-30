# THIS IS QR CODE NUMBER 2

## HERE ARE THE KEY FUNCTIONS TO SOLVE THE SUDOKU BOARD ##
##########################################################

# takes in the board as an array, a row and column as ints, and a number to try to put there
# returns a boolean (True/False)
def isPossible(board, row, col, num):

    # find the top left hand corner of the box that number is in
    topLeftRow = int(row/3)*3
    topLeftCol = int(col/3)*3

    # figure out what numbers are in the little box of nine squares
    alreadyUsed = []
    for r in range(3):
        for c in range(3):
            alreadyUsed.append(board[r+topLeftRow][c+topLeftCol])
    
    # check if there are any conflicts in the square, row, and column
    for i in range(9):
        
        # check the row
        if board[row][i] == num:
            return False
        
        # check the col
        if board[i][col] == num:
            return False
        
        # check the square
        if alreadyUsed[i] == num:
            return False
    
    # if none of those returned false...
    return True

# takes in the board as an array
# returns a boolean (True/False)
def isFilled(board):

    # look through all the spaces and return False if there's an empty space
    for row in range(9):
        for col in range(9):
            if board[row][col] == "_":
                return False

    # if we never found one...
    return True

# prints out all solutions to the sudoku puzzle
# THIS IS THE BACKTRACKING ALGORITHM!!!

def findSolution(board, currentRow, currentCol):

    # the base case
    if isFilled(board):
        print("I found a solution:")
        print()
        printBoard(board)
        return
    
    # find the next empty space
    # search left to right, top to bottom
    while board[currentRow][currentCol] != "_":
        
        if currentCol < 8:
            currentCol = currentCol + 1
        else:
            currentRow = currentRow + 1
            currentCol = 0
    
    # test every number in this space
    # if the number seems to fit, trigger recursion
    for num in range(1, 10):
        
        if isPossible(board, currentRow, currentCol, num):

            # fill in that number
            board[currentRow][currentCol] = num
            
            # advance to the next space
            if currentCol < 8:
                nextRow = currentRow
                nextCol = currentCol + 1
            else:
                nextRow = currentRow + 1
                nextCol = 0
            
            # make the recursive call
            findSolution(board, nextRow, nextCol)

            # remove the number
            board[currentRow][currentCol] = "_"
    
    # once we've tried everything, return
    return

###############################################################



# Here are some boards to test the program with
# They are stored as 9x9 arrays

board1 = [
    [3, "_", 6, 5, "_", 8, 4, "_", "_"],
    [5, 2, "_", "_", "_", "_", "_", "_", "_"],
    ["_", 8, 7, "_", "_", "_", "_", 3, 1],
    ["_", "_", 3, "_", 1, "_", "_", 8, "_"],
    [9, "_", "_", 8, 6, 3, "_", "_", 5],
    ["_", 5, "_", "_", 9, "_", 6, "_", "_"],
    [1, 3, "_", "_", "_", "_", 2, 5, "_"],
    ["_", "_", "_", "_", "_", "_", "_", 7, 4],
    ["_", "_", 5, 2, "_", 6, 3, "_", "_"]
]

board2 = [
    [5, 3, "_", "_", 7, "_", "_", "_", "_"],
    [6, "_", "_", 1, 9, 5, "_", "_", "_"],
    ["_", 9, 8, "_", "_", "_", "_", 6, "_"],
    [8, "_", "_", "_", 6, "_", "_", "_", 3],    
    [4, "_", "_", 8, "_", 3, "_", "_", 1],  
    [7, "_", "_", "_", 2, "_", "_", "_", 6],
    ["_", 6, "_", "_", "_", "_", 2, 8, "_"],
    ["_", "_", "_", 4, 1, 9, "_", "_", 5],  
    ["_", "_", "_", "_", 8, "_", "_", 7, 9]
]

# PRINT THE BOARD NICELY
def printBoard(board):

    for row in range(9):
        
        # check if we need to print a horizontal divider
        if row % 3 == 0:
            for i in range(22):
                print("_", end = "")
            print()

        for col in range(9):

            # check if we need to print a vertical divider
            if col % 3 == 0:
                print("|", end = "")
            
            # print the right space on the board
            print(board[row][col], end = " ")
        
        # at the end of each row, print a vertical divider and move to the next line
        print("|")
    
    # print one last horizonatl divider
    for i in range(22):
        print("_", end = "")
    print()

## CALLING THE FUNCTIONS ##

# change which board or add your own here!
board = board1

print("HERE IS THE STARTING BOARD:")
printBoard(board)
print()
print()

findSolution(board, 0, 0)
