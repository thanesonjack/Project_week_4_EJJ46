import random

def playerinput(stones):
    print("There are " + str(stones) + " stone(s) left")
    
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
    randmonsterinput = random.randint(1,3)
    
    if randmonsterinput == 1:
        stones -= 1
    elif randmonsterinput == 2:
        stones -= 2
    elif randmonsterinput == 3:
        stones -= 3

    print("The monster removed " + str(randmonsterinput) + " stone(s)")
    return stones

def targetedmonsterinput(stones, int):
    if int == 1:
        targmonsterinput = 1
        stones -= 1
    elif int == 2:
        targmonsterinput = 2
        stones -= 2
    elif int == 3:
        targmonsterinput = 3
        stones -= 3

    print("The monster removed " + str(targmonsterinput) + " stone(s)")
    return stones
    




def rundifficulty1():
    print("Welcome to level 3! Given you beat the monster at tic tac toe, it will take it easy this time...")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you won the last level, you get to go first")

    stones = 15

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
    print("Welcome to level 3! Given you drew the monster at tic tac toe, it will be slightly nicer to you this time...")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you drew the last level, you get to go first")

    stones = 15

    while True:
        stones = playerinput(stones)

        if stones <= 0:
            print("congratulations, you won! Now for one last challenge...")
            return True

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

        if stones <= 0:
            print("The monster took the last stone. You lose. start again!")    
            return False

        
def rundifficulty3():
    print("Welcome to level 3! Given you lost to the monster at tic tac toe, you might struggle to win this one lol")
    print("You start with the number 15. You can take away 1, 2, or 3 from the number per turn. The monster will do the same, and whoever takes the last number wins")
    print("As you lost the last level, the monster gets to go first")

    stones = 15

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
        
        if stones <= 0:
            print("The monster took the last stone. You lose. start again!")    
            return False


rundifficulty3()