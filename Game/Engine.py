from Levels import Lvl1
from Levels import Lvl2
from Levels import Lvl3
from Levels import Lvl4


def gameend():
    print("Wow! You somehow made it out? Enjoy this, because it may not happen again!")

def startgame():

    print("Welcome to the game! You will play 4 different levels, each with increasing difficulty. If you fail one, you will have to start from the beginning. Best of luck!")

    lvl1success = Lvl1.run()
    if lvl1success:
        
        lvl2result = Lvl2.run()
        if lvl2result == 1:
            
            lvl3success = Lvl3.rundifficulty1()
            if lvl3success:
                
                lvl4success = Lvl4.run()
                if lvl4success:
                    gameend()
                else:
                    return startgame()
            else:
                return startgame()
            
        elif lvl2result == 2:
            
            lvl3success = Lvl3.rundifficulty2()
            if lvl3success:
                
                lvl4success = Lvl4.run()
                if lvl4success:
                    gameend()
                else:
                    return startgame()
            else:
                return startgame()
            
        elif lvl2result == 3:

            lvl3success = Lvl3.rundifficulty3()
            if lvl3success:
                
                lvl4success = Lvl4.run()
                if lvl4success:
                    gameend()
                else:
                    return startgame()
            else:
                return startgame()
    else:
        return startgame()
    


        


startgame()

    

