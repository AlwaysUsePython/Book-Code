## MINIMAX FUNCTIONS - STRAIGHT FROM THE BOOK! ##

## NOTE: BOOK CHANGES
# get rid of WIN/LOSS/TIE in the sample code and use the strings - just like coins
# Change how the baord is set up -> 3x3 array, "_" instead of " _ "
# I think the book code doesn't work? Lines 98-101 -> need a "LOSS" case

def findBestMove(board, player, debugFlag):
    # I've included a debug flag which will print out what the computer is thinking for both minimax methods

    # set to values that will never be the final answer
    currentBestMove = [0, 0]
    currentBestOutcome = -999

    # loop through the board
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                
                # that means it's a legal move, so find out what happens
                possibleOutcome = whatHappens(board, row, col, player, debugFlag)

                # check if it's better than what we already have
                if isBetter(possibleOutcome, currentBestOutcome):
                    currentBestMove = [row, col]
                    currentBestOutcome = possibleOutcome
    
    # return what was best
    return [currentBestMove, currentBestOutcome]

def whatHappens(board, row, col, player, debugFlag):

    testBoard = generateTestBoard(board, row, col, player)
    outcome = scoreBoard(testBoard)
    
    if debugFlag:
        print("Current variation:")
        printBoard(testBoard)
        print(outcome)
        ready = input("Hit enter to continue:")
        print()

    # Note: it's impossible to make a move and lose by placing your move. You can't get 3 in a row for your opponent with your own piece
    if outcome == "WIN" or outcome == "TIE":
        return outcome

    # if the game didn't end, find out what the opponent will do
    if player == "C":
        player = "P"
    else:
        player = "C"
    
    opponentResult = findBestMove(testBoard, player, debugFlag)[1]

    # return the opposite perspective of what the opponent thought would happen
    if opponentResult == "WIN":
        return "LOSS"
    if opponentResult == "TIE":
        return "TIE"
    else:
        return "WIN"

#######################################################################################

# UTILITY FUNCTIONS

def printBoard(board):
    for row in board:
        for col in row:
            print(col, end = " ")
        print()
    print()

def scoreBoard(board):
    # Input: the board (as a 3x3 array)
    # Output: the result of that board (ASSUMING NO FURTHER MOVES)
    # possible returns: "WIN", "TIE", "UNFINISHED"

    # keep track of if the board is full
    fullBoard = True

    # check the rows for 3 in a row
    for row in range(3):
        
        # check blank spaces
        for col in range(3):
            if board[row][col] == "_":
                fullBoard = False
        
        # check for 3 in a row
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
            return "WIN"

    # same for columns except we already know if it's a full board or not
    for col in range(3):
        
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
            return "WIN"

    # check the 2 diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
        return "WIN"
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != "_":
        return "WIN"

    # if the board was full, return "TIE"
    if fullBoard:
        return "TIE"

    # if it wasn't a tie and no one won, return "UNFINISHED"
    return "UNFINISHED"

def generateTestBoard(board, row, col, player):
    # INPUT: the current board, the row/col of the space to add a piece to, and which piece to add
    # OUTPUT: a board

    # copy the board -> avoid potential errors in the future
    newBoard = []
    for r in board:
        newBoard.append(copyList(r))

    newBoard[row][col] = player
    return newBoard

def copyList(list):
    # INPUT: a list
    # OUTPUT: a copy of that list
    # why!?? avoiding errors

    # if I set variable1 equal to list a and variable 2 equal to variable 1, editing either variable1 or variable2 will edit list a which edits both of them
    # that's a headache and a half. So we're going to avoid that by using this copy list function

    newList = []

    for item in list:
        newList.append(item)
    
    return newList

def isBetter(outcome1, outcome2):
    # If outcome1 is better than outcome2 or the same as outcome2, returns True
    # otherwise returns false
    
    if outcome1 == "WIN":
        return True
    
    elif outcome2 == "WIN":
        return False
    
    elif outcome1 == "TIE":
        return True
    
    elif outcome1 == "TIE":
        return False
    
    else:
        return True

#######################################################################################

# MAIN PROGRAM

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

turn = "P"

while scoreBoard(board) == "UNFINISHED":
    print()
    printBoard(board)
    
    print()
    print(turn, "TO PLAY!")
    print()

    if turn == "P":

        # make sure they don't cheat
        validMove = False

        while not validMove:
            row = int(input("What row? (1, 2, 3) ")) - 1
            col = int(input("What col? (1, 2, 3) ")) - 1

            if board[row][col] == "_":
                validMove = True

    
    else:
        
        debug = input("Do you want me to show my steps? warning: if it's an early move, this will be a bit overwhelming (y/n) ")
        
        if debug == "y":
            debugFlag = True
        else:
            debugFlag = False

        move = findBestMove(board, "C", debugFlag)

        row = move[0][0]
        col = move[0][1]
        print(move[1])

        print("The computer chose", row, col)
    
    board[row][col] = turn

    currentState = scoreBoard(board)
    
    if currentState == "WIN":
        print(turn, "WINS!")
    
    elif currentState == "TIE":
        print("It's a tie!")

    if turn == "P":
        turn = "C"
    else:
        turn = "P"

printBoard(board)