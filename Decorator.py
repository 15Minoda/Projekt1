class Component():
    def Operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def Operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None


    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component
    
    def Operation(self) -> str:
        return self._component.Operation()

class ConcreteDecoratorA(Decorator):

    def Operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.Operation()})"

class ConcreteDecoratorB(Decorator):

    def Operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.Operation()})"


def ClientCode(component : Component) -> None:
    print(f"RESULT: {component.Operation()}", end="")
    pass



#Interface PizzaBelag
class Pizza():
    """Interface for Decorator"""
    def ExtraBelag(self) -> str:
        pass

    def ExtraPreis(self) -> int:
        pass 

class PizzaBoden(Pizza):
    def ExtraBelag(self) -> str:
        return "Pizzaboden"

    def ExtraPreis(self) -> int:
        return 4

# Interface Dekorierer
class Belag(Pizza):
    _belag : Pizza = None

    def __init__(self, belag: Pizza) -> None:
        self._belag = belag

    @property
    def belag(self) -> str:
        return self._belag
    
    def ExtraBelag(self) -> str:
        return self._belag.ExtraBelag()

    def ExtraPreis(self) -> int:
        return self.ExtraPreis()

class ExtraSalami(Belag):
    def ExtraBelag(self) -> str:
        return super().ExtraBelag() + " + Extra Salami"

    def ExtraPreis(self) -> int:
        return super().ExtraPreis() + 1

class ExtraCheese(Belag):
    def ExtraBelag(self) -> str:
        return super().ExtraBelag() + " + Extra Kase"

    def ExtraPreis(self) -> int:
        return super().ExtraPreis() + 2


    
