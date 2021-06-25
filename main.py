import Module1 

def main():
    print("Hello")

    Mino = Module1.Human("Minoda", 20)

    Mino.AddExp(20)
    Mino.AddExp(80)
    Mino.SubHP(18)
    
    Mino.SubHP(3)
    Mino.Show



if __name__ == '__main__':
    main()