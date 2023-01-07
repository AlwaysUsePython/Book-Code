
# Create an empty maze – the " " is an empty space

maze = [
  ["s", "◻️", " ", "◻️", " "], 
  [" ", " ", " ", " ", " "], 
  [" ", "◻️", "◻️", " ", "◻️"], 
  [" ", " ", "◻️", " ", " "], 
  [" ", " ", " ", "◻️", " "]]

# This is the print board function but maze
def printMaze(maze):
  for row in maze:
    for item in row:
      print(item, end = " ")
    print()


#printMaze(maze)

# This function takes in parameters of a maze, a position (row, col) and a direction. 
# To make things easy, I am using numbers to represent directions. 1 is North, 2 is East, 3 is South, and 4 is West
def isPossible(maze, row, col, direction):
  # for each direction, i need an if statement

  # if it's north
  if direction == 1:
    # if I can go North while staying on the board
    if row - 1 >= 0:
      # If there is no wall in my way
      if maze[row-1][col] == " ":
        return True
  
  # All of these are the same as the one I did for North except different directions
  elif direction == 2:
    if col + 1 < 5:
      if maze[row][col + 1] == " ":
        return True
  elif direction == 3:
    if row + 1 < 5:
      if maze[row+1][col] == " ":
        return True
  else:
    if col - 1 >= 0:
      if maze[row][col-1] == " ":
        return True
  # if the direction wasn't possible (if we haven't already returned True)
  # then we return False
  return False


# Recursion! Backtracking! Yay!
# This function inputs the maze, the starting row, and the starting col
def solveMaze(maze, startRow, startCol):
  printMaze(maze)
  ready = input("Hit enter for next move: ")
  print()
  print("_________________________________")
  print()
  # If we get to the end of the maze, print the solution
  if startRow == 4 and startCol == 4:
    print("I found a solution!")
    printMaze(maze)
    ready = input("Hit enter to continue searching: ")
    print()
    print("_________________________________")
    print()

  # For each possible direction we could try
  for direction in range(1, 5):
    # If we can go that direction
    if isPossible(maze, startRow, startCol, direction):
      # we need an if statement for each direction
      if direction == 1:
        # Make our guess with an * in that direction
        maze[startRow-1][startCol] = "*"
        # Try to solve the maze starting at the square we just filled in
        solveMaze(maze, startRow-1, startCol)
        # If that doesn't work, backtrack!
        maze[startRow-1][startCol] = " "
      # all of the others are the same as the direction 1 one
      elif direction == 2:
        maze[startRow][startCol+1] = "*"
        solveMaze(maze, startRow, startCol+1)
        maze[startRow][startCol+1] = " "
      elif direction == 3:
        maze[startRow+1][startCol] = "*"
        solveMaze(maze, startRow+1, startCol)
        maze[startRow+1][startCol] = " "
      else:
        maze[startRow][startCol-1] = "*"
        solveMaze(maze, startRow, startCol-1)
        maze[startRow][startCol-1] = " "
  # This return tells the computer to stop and go back once it tests all the possible directions for a space
  return

print()
solveMaze(maze, 0, 0)
