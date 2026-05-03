import random

def playerinput(stones):
    """
    Defines player input for the game, taking how many stones they want to remove as well as checking validity of input
    """
    
    #tell player how many remain
    print("There are " + str(stones) + " stone(s) left")
    
    #Take player input, removing corresponding number of stones, and rejecting if input is invalid
    stoneinput = input("How many stones do you wish to remove? ")
    if stoneinput == "1":
            stones -= 1
            print("There are " + str(stones) + " stone(s) left")
            return stones
    elif stoneinput == "2":
            stones -= 2
            print("There are " + str(stones) + " stone(s) left")
            return stones
    elif stoneinput == "3":
            stones -= 3
            print("There are " + str(stones) + " stone(s) left")
            return stones
    else:
            print("Invalid input, must be 1, 2, or 3")
            return playerinput(stones)

def randmonsterinput(stones):
    """
    Defines the random input for the monster, crucial for different difficulty levels
    """

    #Generate random integer between 1 and 3
    randmonsterinput = random.randint(1,3)
    
    #Remove corresponding number of stones
    if randmonsterinput == 1:
        stones -= 1
    elif randmonsterinput == 2:
        stones -= 2
    elif randmonsterinput == 3:
        stones -= 3

    # Print how many stones have been removed
    print("The monster removed " + str(randmonsterinput) + " stone(s)")

    #Return remaining stones
    return stones

def targetedmonsterinput(stones, int):
    """
    Defines targeted inputs for higher diffculty levels to allow monster to win
    """
    
    #If input is 1, 2 or 3 return corresponding number of stones
    if int == 1:
        targmonsterinput = 1
        stones -= 1
    elif int == 2:
        targmonsterinput = 2
        stones -= 2
    elif int == 3:
        targmonsterinput = 3
        stones -= 3

    # Print how many stones have been removed
    print("The monster removed " + str(targmonsterinput) + " stone(s)")

    #Return remaining stones
    return stones
    




def rundifficulty1():
    """
    Sets out difficulty level 1- monster makes completely random moves
    """

    # Intro message
    print("Welcome to level 3! Given you beat the monster at tic tac toe, it will take it easy this time...")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you won the last level, you get to go first")

    # Initial number of stones
    stones = 15

    #Main game loop, taking player and monster inputs until one wins
    while True:
        stones = playerinput(stones)
        
        if stones <= 0:
            print("Congratulations, you won! Now for one last challenge...")
            return True       
    
        stones = randmonsterinput(stones)
    
        if stones <= 0:
            print("The monster took the last stone. You lose. start again!")    
            return False
        
        
             
def rundifficulty2():
    """
    Sets out difficulty level 2, where monster makes random moves early game but targeted moves when stones get below 7- player must realise this to win
    """

    #Level intro message
    print("Welcome to level 3! Given you drew the monster at tic tac toe, it will be slightly nicer to you this time...")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you drew the last level, you get to go first")

    #Initialise number of stones
    stones = 15

    #standard game loop with player and monster taking turns
    while True:
        stones = playerinput(stones)

        #Condition for player winning
        if stones <= 0:
            print("congratulations, you won! Now for one last challenge...")
            return True

        #Once stones get to 7, monster makes targeted moves specifically to win
        if stones > 7:
            stones = randmonsterinput(stones)
        elif stones == 7:
            stones = targetedmonsterinput(stones, 3)
        elif stones == 6:
            stones = targetedmonsterinput(stones, 2)
        elif stones == 5:
            stones = targetedmonsterinput(stones, 1)
        elif stones == 4:
            stones = randmonsterinput(stones)
        elif stones == 3:
            stones = targetedmonsterinput(stones, 3)
        elif stones == 2: 
            stones = targetedmonsterinput(stones, 2)
        elif stones == 1:
            stones = targetedmonsterinput(stones, 1)

        #condition for monster winning
        if stones <= 0:
            print("The monster took the last stone. You lose. start again!")    
            return False

        
def rundifficulty3():
    """
    Dictates hardest level of difficulty- impossible for player to win as monster starts and instantly jumps for multiples of 4
    """

    #Intro message
    print("Welcome to level 3! Given you lost to the monster at tic tac toe, you might struggle to win this one lol")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you lost the last level, the monster gets to go first")

    #Initialise number of stones
    stones = 15

    #While loop, taking every possible player move and outputting corresponding monster move such that player cannot win
    while True:
        stones = targetedmonsterinput(stones, 3)

        stones = playerinput(stones)
        
        if stones == 11:
            stones = targetedmonsterinput(stones, 3)
        elif stones == 10:
            stones = targetedmonsterinput(stones, 2)
        elif stones == 9:
            stones = targetedmonsterinput(stones, 1)
        
        stones = playerinput(stones)

        if stones == 7:
            stones = targetedmonsterinput(stones, 3)
        elif stones == 6:
            stones = targetedmonsterinput(stones, 2)
        elif stones == 5:
            stones = targetedmonsterinput(stones, 1)
        
        stones = playerinput(stones)

        if stones == 3:
            stones = targetedmonsterinput(stones, 3)
        elif stones == 2:
            stones = targetedmonsterinput(stones, 2)
        elif stones == 1:
            stones = targetedmonsterinput(stones, 1)
        
        #win condition for monster
        if stones <= 0:
            print("The monster took the last stone. You lose. start again!")    
            return False


