import Items 
import Enteties
import ObserverPattern_Test
import Decorator

from datetime import datetime

now = datetime.now()
DEBUG = 1

def Test():
    print("welcome to Test")

def main():
    print("Hello new Start "+ str(now))

    Mino = Enteties.Human("Minoda", 50, DEBUG)
    #Test = Enteties.Creature("testvieh", 50, DEBUG)

    #Test.AddExp(200)
    Mino.AddExp(20)
    Mino.AddExp(80)
    Mino.SubHP(18)
    Mino.AddExp(5000)
    #Test.AddExp(5000)
    Mino.SubHP(500)
    #Test.Show()
    Mino.Show()

    

if __name__ == '__main__':
    #Test()
    main()