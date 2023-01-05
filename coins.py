
## MINIMAX FUNCTIONS - STRAIGHT FROM THE BOOK! ##

## NOTE: BOOK CHANGE
# get rid of WIN in the sample code and use the string "WIN"

def findBestMove(coins):

    outcomeOne = whatHappens(coins, 1)
    outcomeTwo = whatHappens(coins, 2)

    if outcomeOne == "WIN":
        return [1, outcomeOne]
    
    else:
        return [2, outcomeTwo]

def whatHappens(coins, move):

    newStatus = coins - move

    if newStatus <= 0:
        return "WIN"
    
    opponentOutcome = findBestMove(newStatus)[1]

    if opponentOutcome == "WIN":
        return "LOSE"
    
    else:
        return "WIN"

# Initialize the number of coins
coins = 9

print("There are 9 coins to start. On each turn, you can take one or two coins.")
print("The computer goes second. Whoever takes the last coin wins!")
print()

# Make a game loop with turns
turn = "PLAYER"

while coins > 0:
    print(turn, "TO MOVE...")
    print("There are", coins, "coins left.")
    print()
    
    if turn == "PLAYER":
        choice = int(input("1 or 2? "))
        print()
    
    else:
        choice = findBestMove(coins)[0]
        print("The computer took", choice, "coins.")
        print()
    
    
    coins -= choice
    if coins <= 0:
        print(turn, "WINS!")

    # SWITCH TURN
    if turn == "PLAYER":
        turn = "COMPUTER"
    else:
        turn = "PLAYER"