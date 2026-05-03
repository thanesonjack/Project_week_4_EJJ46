# Generate board
tictactoe = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]

def printboard():
    """
    Prints tic tac toe board with current state of game
    """
    # Print board
    for row in tictactoe:
        print(" ".join(row))
    

def playerinput():
    """
    Takes player input and updates board
    """
    #take input and check if valid- cannot place an x on an already taken spot
    tttinput = input("Enter numbers 1-9 to place your x, corresponding to the numpad on a keybord")
    if tttinput == "1":
        if tictactoe[2][0] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[2][0] = "X"
    elif tttinput == "2":
        if tictactoe[2][1] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[2][1] = "X"
    elif tttinput == "3":
        if tictactoe[2][2] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[2][2] = "X"
    elif tttinput == "4":
        if tictactoe[1][0] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[1][0] = "X"
    elif tttinput == "5":
        if tictactoe[1][1] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[1][1] = "X"
    elif tttinput == "6":
        if tictactoe[1][2] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[1][2] = "X"
    elif tttinput == "7":
        if tictactoe[0][0] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[0][0] = "X"
    elif tttinput == "8":
        if tictactoe[0][1] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[0][1] = "X"
    elif tttinput == "9":
        if tictactoe[0][2] == "X":
            print("That spot is already taken, try again")
            return playerinput()
        tictactoe[0][2] = "X"
    else:
        print("Invalid input, try again")

        return tttinput

def possiblemoves():
    """
    Defines all possible moves the monster can make
    """
    #Create a list of possible moves by checking blank spaces on board and appending to list
    moves = []
    for r in range(3):
        for c in range(3):
            if tictactoe[r][c] == "_":
                moves.append((r, c))
    return moves

def monsterinput():
    """
    Outputs random monster input, adding to the board
    """

    import random

    #Check possible coordinates for O
    moves = possiblemoves()

    #Case for if no moves are left
    if not moves:
        return

    # Place an O in random spot from available moves
    r,c = random.choice(moves)
    tictactoe[r][c] = "O"


def fullboard():
    """
    Sets out conditions for if the board is full, resulting in a draw
    """
    #If player hasn't won, and no more moves are possible, it is a draw
    if not wincondition():
        if len(possiblemoves()) == 0:
            print("It's a draw!")
            return True
        return False
    
def wincondition():
    """
    Sets out win conditions for if either player has won
    """

    #Sort through all possible win conditions, for both players, returning whoever wins, or false if no win yet
    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
        return "X"
    elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
        return "X"
    elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
        return "X"
    elif tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
        return "X"
    elif tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
        return "X"
    elif tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X":
        return "X"
    elif tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X":
        return "X"
    elif tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
        return "X"
    elif tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
        return "X"
    elif tictactoe[0][0] == "O" and tictactoe[0][1] == "O" and tictactoe[0][2] == "O":
        return "O"
    elif tictactoe[1][0] == "O" and tictactoe[1][1] == "O" and tictactoe[1][2] == "O":
        return "O"
    elif tictactoe[2][0] == "O" and tictactoe[2][1] == "O" and tictactoe[2][2] == "O":
        return "O"
    elif tictactoe[0][0] == "O" and tictactoe[1][0] == "O" and tictactoe[2][0] == "O":
        return "O"
    elif tictactoe[0][1] == "O" and tictactoe[1][1] == "O" and tictactoe[2][1] == "O":
        return "O"
    elif tictactoe[0][2] == "O" and tictactoe[1][2] == "O" and tictactoe[2][2] == "O":
        return "O"
    elif tictactoe[0][0] == "O" and tictactoe[1][1] == "O" and tictactoe[2][2] == "O":
        return "O"
    elif tictactoe[0][2] == "O" and tictactoe[1][1] == "O" and tictactoe[2][0] == "O":
        return "O"
    else:
        return False



def run():
    """
    Runs level 2 ofthe game, taking playerinput function and feeding into wincondition/fullboard/printboard functions to correctly run the game
    """
    #Intro message
    print("You made it through level 1? Well, you're not done yet! In this level, you need to play the monster at tic tac toe to make it through. You go first, good luck!")

    # Main game loop. returning 1 if player wins, 2 if draw, and 3 if monster wins
    while True:
        printboard()
        playerinput()
        
        winner = wincondition()
        if winner == "X":
            printboard()
            print("Congratulations, you win! The next level may be slightly easier...")
            return 1       #easy difficulty

        if fullboard():
            Lvl3difficulty = 2
            printboard()
            print("It's a draw. Progress if you dare...")
            return 2     #medium difficulty

        monsterinput()

        winner = wincondition()
        if winner == "O":
            Lvl3difficulty = 3
            printboard()
            print("The monster wins! You may struggle with the next level...")
            return 3     #hard difficulty

        if fullboard():
            Lvl3difficulty = 2
            printboard()
            print("It's a draw. Progress if you dare...")
            return 2     #medium difficulty            

    


    


