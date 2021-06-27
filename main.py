import Items 
import Enteties
import Observer
import Decorator

from datetime import datetime

now = datetime.now()
DEBUG = 1


def ObserverTest():
    pass


def DecoratorTest():
    print("welcome to Decorator")

    MeinePizza = Decorator.PizzaBoden()
    print(f"meine Pizza  {MeinePizza.ExtraBelag()}")

    KasePizza = Decorator.ExtraCheese(MeinePizza)

    print(f"Meine neue Pizza  {KasePizza.ExtraBelag()}")

    SalamiKasePizza = Decorator.ExtraSalami(KasePizza)

    print(f"Meine neue Pitta {SalamiKasePizza.ExtraBelag()}")
    
   # print("Meine neue Pitta "+ str(SalamiKasePizza.ExtraPreis()))

    SalamiKasePizza = Decorator.ExtraSalami(SalamiKasePizza)

    print(f"Meine neue Pizza {SalamiKasePizza.ExtraBelag()}")

    # simple = Decorator.ConcreteComponent()
    # print("Client: i have a component")
    # Decorator.ClientCode(simple)
    # print("\n")

    # decorator1 = Decorator.ConcreteDecoratorA(simple)
    # decorator2 = Decorator.ConcreteDecoratorB(decorator1)

    # print("Client is decorated")

    # Decorator.ClientCode(decorator2)


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
    DecoratorTest()
    #main()
    #ObserverTest()