from Game.Levels import Lvl1
from Game.Levels import Lvl2
from Game.Levels import Lvl3
from Game.Levels import Lvl4
from Game.Levels import Lvl5



def startgame():
    print("Insert intro text here")

    lvl1pass = Lvl1.run()

    if lvl1pass: 
        print("Insert lvl2 intro text here")
    else:
        print("you die!")

        lvl2pass = Lvl2.run()

        if lvl2pass:
            print("Insert lvl3 intro text here")
        else:
            print("you die!")

            lvl3pass = Lvl3.run()

            if lvl3pass:
                print("Insert lvl4 intro text here")
            else:
                print("you die!")

                lvl4pass = Lvl4.run()

                if lvl4pass:
                    print("Insert lvl5 intro text here")
                else:
                    print("you die!")

                    lvl5pass = Lvl5.run()

                    if lvl5pass:
                        print("Insert game ending text here")
                    else:
                        print("you die!")


