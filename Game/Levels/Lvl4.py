import random

def correctcode():
    """
    Generates a random 4 digit code
    """
    
    #Create empty list
    code = []
    
    #Populate list with 4 random digits
    codedigit1 = random.randint(0,9)
    code.append(codedigit1)

    codedigit2 = random.randint(0,9)
    code.append(codedigit2)

    codedigit3 = random.randint(0,9)
    code.append(codedigit3)

    codedigit4 = random.randint(0,9)
    code.append(codedigit4)


    #Return code
    return code

def playerattempt():
    """
    Takes player input and converts to string as well as list of integers. Checks for validity of input and returns list of integers
    """

    #Player input
    attempt = input("Enter a 4 digit code")

    #Convert to string
    input_string = str(attempt)

    #Conditions for invalid input
    if not attempt.isdigit() or len(attempt) != 4:
        print("Invalid input, must be a 4 digit number")
        return playerattempt()

    # Return list of integers
    return [int(d) for d in attempt]

def attemptcheck(input_string,code):
    """
    Checks player input against correct code, outputting list showing whether digits are correct and in the right place
    """

    #Create empty list to store values
    checklist = [0, 0, 0, 0]

    # crossreference each digit of player input against correct code, outputting Y, M or X according to validity
    if input_string[0] == code[0]:
        checklist[0] = "Y"
    elif input_string[0] == code [1] or input_string[0] == code [2] or input_string[0] == code [3]:
        checklist[0] = "M"
    else:
        checklist[0] = "X"

    if input_string[1] == code[1]:
        checklist[1] = "Y"
    elif input_string[1] == code [0] or input_string[1] == code [2] or input_string[1] == code [3]:
        checklist[1] = "M"
    else:
        checklist[1] = "X"

    if input_string[2] == code[2]:
        checklist[2] = "Y"
    elif input_string[2] == code [0] or input_string[2] == code [1] or input_string[2] == code [3]:
        checklist[2] = "M"
    else:
        checklist[2] = "X"

    if input_string[3] == code[3]:
        checklist[3] = "Y"
    elif input_string[3] == code [0] or input_string[3] == code [1] or input_string[3] == code [2]:
        checklist[3] = "M"
    else:
        checklist[3] = "X"

    #Show player the results
    print(checklist)

    #Return checklist
    return checklist

    


def run():
    """
    Runs level 4, generating code, taking player input and checking against correct code until player wins or runs out of attempts
    """

    #Intro message
    print("Welcome to level 4! You have escaped the monster, but have one more task- crack the code to the door. You have 10 attempts to guess the 4 digit code. Y means the digit is in the correct position, M means the digit is in the code but not in the correct position, and X means the digit is not in the code at all.")

    #generate code
    code = correctcode()

    #Set amount of attemps
    totalattempts = 10

    #While loop, taking player input and checking for 10 attempts unless player wins
    while totalattempts > 0:
        attempt = playerattempt()
        attemptcheck(attempt, code)

        if attempt == code:
            print("Level 4 completed!")
            return True
        else:
            totalattempts -= 1
            print("Incorrect code, you have " + str(totalattempts) + " attempts left")
        
    #Losing condition
    if totalattempts == 0:
        print("Oh dear, you have fallen at the final hurdle. You have run out of attemps. You die of starvation, desparately close to escaping the prison.")

