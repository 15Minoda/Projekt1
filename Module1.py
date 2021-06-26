class LivingThing():
    __level   = 0
    __actHP   = 0
    __nextExp = 0

    def __init__ (self, name, maxHP):
        self.name   = name
        self.exp    = 0
        self.__maxHP  = maxHP
        self.__actHP  = maxHP    
        self.__nextExp = 100;  
        print("Name: "+self.name+" Level: "+str(self.__level))
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        print("Was Created!")

    def Show (self):
        print("Name: "+self.name+"Level: "+str(self.__level))
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))

    def __LevelUp(self):
        self.__level += 1
        print("Level Up! ->"+str(self.__level))
        self.__nextExp *= self.__level * 1.89
        self.__maxHP += 50

    def __del__(self):
        print(self.name+" was Removed")

    def AddExp(self, exp):
        self.exp += exp
        print("+"+str(exp)+"EXP")
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        if self.exp >= self.__nextExp:
            self.__LevelUp()

    def SubHP(self, val):
        self.__actHP -= val
        print("HP decreased: "+str(val))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        if self.__actHP <= 0:
            print(self.name+" is Dead")
            self.__del__()
    

class Human(LivingThing):
    __level   = 0
    __actHP   = 0
    __nextExp = 0

    def __init__(self, name, maxHP):
        super().__init__(name, maxHP)       

    def __LevelUp(self):
        self.__level += 1
        print("Level Up! ->"+str(self.__level))
        self.__nextExp *= self.__level * 2.5
        self.__maxHP *= 1.2

