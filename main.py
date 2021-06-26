import Module1 
import ObserverPattern_Test#
import Decorator

from datetime import datetime

now = datetime.now()

def main():
    print("Hello new Start "+ str(now))

    Mino = Module1.Human("Minoda", 50)
    #Test = Module1.LivingThing("testvieh", 50)

    #Test.AddExp(200)
    print("action1")
    Mino.AddExp(20)
    print("action2")
    Mino.AddExp(80)
    print("action3")
    Mino.SubHP(18)
    print("action4")
    Mino.AddExp(5000)
    print("action5")
    Mino.SubHP(3)
    print("action6")
    #Test.SubHP(30)
    Mino.Show()



if __name__ == '__main__':
    main()