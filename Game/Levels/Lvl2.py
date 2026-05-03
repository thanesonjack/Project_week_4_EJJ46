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

    if not moves:
        return

    r,c = random.choice(moves)
    tictactoe[r][c] = "O"


def fullboard():
    if not wincondition():
        if len(possiblemoves()) == 0:
            print("It's a draw!")
            return True
        return False
    
def wincondition():
    Lvl3difficulty = 0

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

    print("You made it through level 1? Well, you're not done yet! In this level, you need to play the monster at tic tac toe to make it through. You go first, good luck!")

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
            

    

run()
    


