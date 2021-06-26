import Module1 
import ObserverPattern_Test
import Decorator

from datetime import datetime

now = datetime.now()
DEBUG = 1

def main():
    print("Hello new Start "+ str(now))

    Mino = Module1.Human("Minoda", 50, DEBUG)
    Test = Module1.Creature("testvieh", 50, DEBUG)

    Test.AddExp(200)
    Mino.AddExp(20)
    Mino.AddExp(80)
    Mino.SubHP(18)
    Mino.AddExp(5000)
    #Test.AddExp(5000)
    Mino.SubHP(500)
    #Test.Show()
    Mino.Show()



if __name__ == '__main__':
    main()