import Module1 

def main():
    print("Hello")

    Mino = Module1.Human("Minoda", 20)
    Test = Module1.LivingThing("testvieh", 50)

    Test.AddExp(200)
    Mino.AddExp(20)
    Mino.AddExp(80)
    Mino.SubHP(18)
    Mino.AddExp(90)
    Mino.SubHP(3)
    Test.SubHP(30)
    Mino.Show



if __name__ == '__main__':
    main()