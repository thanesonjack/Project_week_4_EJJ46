#Import levels
from Game.Levels import Lvl1
from Game.Levels import Lvl2
from Game.Levels import Lvl3
from Game.Levels import Lvl4


def gameend():
    """
    Prints end message for game when player completes every level
    """

    #Print message
    print("Wow! You somehow made it out? Enjoy this, because it may not happen again!")

def startgame():
    """
    Starts game, running through each level. If player fails a level, they have to start from the beginning. 
    Facilitates difficulty levels for level 3, based on result of level 2
    """
    #game intro message
    print("Welcome to the game! You will play 4 different levels, each with increasing difficulty. If you fail one, you will have to start from the beginning. Best of luck!")

    #Run level 1
    lvl1success = Lvl1.run()
    if lvl1success:
        
        #run level 2 based on if player completes level 1
        lvl2result = Lvl2.run()
        if lvl2result == 1:
            
            #run level 3 at difficulty 1 if player wins level 2
            lvl3success = Lvl3.rundifficulty1()
            if lvl3success:
                
                #run level 4 if player wins level 3
                lvl4success = Lvl4.run()
                
                #end game if player wins level 4
                if lvl4success:
                    gameend()
                
                #restart if failure at level 4
                else:
                    return startgame()
            
            #restart if failure at level 3
            else:
                return startgame()


        elif lvl2result == 2:
            
            #run level 3 at difficulty 2 if player draws level 2
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
            
            #run level 3 at difficulty 3 if player loses level 2
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
    


