tictactoe = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]

def printboard():
    for row in tictactoe:
        print(" ".join(row))
    

def playerinput():
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
    moves = []
    for r in range(3):
        for c in range(3):
            if tictactoe[r][c] == "_":
                moves.append((r, c))
    return moves

def monsterinput():
    import random

    moves = possiblemoves()

    r,c = random.choice(moves)
    tictactoe[r][c] = "O"


def fullboard():
    if len(possiblemoves()) == 0:
        print("It's a draw!")
        return True
    return False
    
def wincondition():
    if tictactoe[0][0] == "X" and tictactoe[0][1] == "X" and tictactoe[0][2] == "X":
        print("You win!")
        return True
    elif tictactoe[1][0] == "X" and tictactoe[1][1] == "X" and tictactoe[1][2] == "X":
        print("You win!")
        return True
    elif tictactoe[2][0] == "X" and tictactoe[2][1] == "X" and tictactoe[2][2] == "X":
        print("You win!")
        return True
    elif tictactoe[0][0] == "X" and tictactoe[1][0] == "X" and tictactoe[2][0] == "X":
        print("You win!")
        return True
    elif tictactoe[0][1] == "X" and tictactoe[1][1] == "X" and tictactoe[2][1] == "X":
        print("You win!")
        return True
    elif tictactoe[0][2] == "X" and tictactoe[1][2] == "X" and tictactoe[2][2] == "X":
        print("You win!")
        return True
    elif tictactoe[0][0] == "X" and tictactoe[1][1] == "X" and tictactoe[2][2] == "X":
        print("You win!")
        return True
    elif tictactoe[0][2] == "X" and tictactoe[1][1] == "X" and tictactoe[2][0] == "X":
        print("You win!")
        return True
    else:
        return False



def run():

    print("You made it through level 1? Well, you're not done yet! In this level, you need to play the monster at tic tac toe to make it through. You go first, good luck!")

    while not wincondition():
        printboard()
        playerinput()
        if fullboard():
            break
            return False
        monsterinput()
    if wincondition():
        printboard()
        print("You win! Level complete!")
        return True
    

run()
    


