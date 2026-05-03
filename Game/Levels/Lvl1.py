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
    
    row, col = position
    
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

    print("Welcome to level 1! You are in a maze, but are blindfolded and can only see the maze at the start of the level. Memorise the correct inputs, using WASD, and find your way to the end of the maze!")

    for row in maze:
        print(" ".join(row))

    position = (1, 0)

    while True:
        direction = input("Enter direction (WASD): ")
        new_position = playermovement(position, direction)

        if maze[new_position[0]][new_position[1]] == "X":
            print("You hit a wall! You die.")
            return False
        elif maze[new_position[0]][new_position[1]] == "->":
            print("You found the exit! Level complete!")
            return True
        else:
            position = new_position


run()