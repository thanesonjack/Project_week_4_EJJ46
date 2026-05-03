import random

def correctcode():
    code = []
    
    codedigit1 = random.randint(0,9)
    code.append(codedigit1)

    codedigit2 = random.randint(0,9)
    code.append(codedigit2)

    codedigit3 = random.randint(0,9)
    code.append(codedigit3)

    codedigit4 = random.randint(0,9)
    code.append(codedigit4)



    return code

def playerattempt():
    attempt = input("Enter a 4 digit code")
    input_string = str(attempt)

    if not attempt.isdigit() or len(attempt) != 4:
        print("Invalid input, must be a 4 digit number")
        return playerattempt()


    return [int(d) for d in attempt]

def attemptcheck(input_string,code):
    
    checklist = [0, 0, 0, 0]

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

    print(checklist)

    return checklist

    


def run():

    print("Welcome to level 4! You have escaped the monster, but have one more task- crack the code to the door. You have 10 attempts to guess the 4 digit code. Y means the digit is in the correct position, M means the digit is in the code but not in the correct position, and X means the digit is not in the code at all.")

    code = correctcode()

    totalattempts = 10

    while totalattempts > 0:
        attempt = playerattempt()
        attemptcheck(attempt, code)

        if attempt == code:
            print("Level 4 completed!")
            return True
        else:
            totalattempts -= 1
            print("Incorrect code, you have " + str(totalattempts) + " attempts left")
        
    if totalattempts == 0:
        print("Oh dear, you have fallen at the final hurdle. You have run out of attemps. You die of starvation, desparately close to escaping the prison.")

