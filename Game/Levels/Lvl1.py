# Generate maze
maze = [
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    [">", ".", "X", ".", ".", "X", ".", "X"],
    ["X", ".", ".", ".", "X", ".", ".", "X"],
    ["X", ".", "X", "X", "X", ".", "X", "X"],
    ["X", ".", ".", "X", ".", ".", ".", "X"],
    ["X", "X", ".", "X", ".", "X", ".", "X"],
    ["X", ".", ".", ".", ".", "X", ".", "->"],
    ["X", "X", "X", "X", "X", "X", "X", "X"]
]

def playermovement(position, direction):
    """
    Moves player in desired direction
    """
    # Define row and column variables
    row, col = position
    
    #Take directional input and move player according to which way they want to go
    if direction == "W":
        return (row-1, col)
    if direction == "A":
        return (row, col-1)
    if direction == "S":
        return (row+1, col)
    if direction == "D":
        return (row, col+1)
    else:
        print("Invalid input!")
        return position
    
def run():
    """
    Runs first level of the game, taking players input and feeding that into playermovement until they win or lose
    """
    print("Welcome to level 1! You are in a maze, but are blindfolded and can only see the maze at the start of the level. Memorise the correct inputs, using WASD, and find your way to the end of the maze!")
    
    # Display maze
    for row in maze:
        print(" ".join(row))

    # Set initial position
    position = (1, 0)

    # While loop, taking players input and making use of the playermovement function
    while True:
        direction = input("Enter direction (WASD): ")
        new_position = playermovement(position, direction)

        # Player failure or success
        if maze[new_position[0]][new_position[1]] == "X":
            print("You hit a wall! You die.")
            return False
        elif maze[new_position[0]][new_position[1]] == "->":
            print("You found the exit! Level complete!")
            return True
        else:
            position = new_position


