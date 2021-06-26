class LivingThing():
    __actHP   = 0
    __nextExp = 0
    actionCounter = 0

    def __init__ (self, name, maxHP, debug = 0):
        self.debug = debug
        self.__level   = 0
        self.name   = name
        self.exp    = 0
        self.__maxHP  = maxHP
        self.__actHP  = maxHP    
        self.__nextExp = 100;  
        print("##############################################")
        print("Name: "+self.name+" Level: "+str(self.__level))
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        print("Was Created!")
        print("##############################################")

    def NewAction(self):
        if self.debug > 0:
            LivingThing.actionCounter+=1
            print("--------------------Action_"+str(LivingThing.actionCounter))

    def Show (self):
        self.NewAction()
        print("##############################################")
        print("Name: "+self.name+" Level: "+str(self.__level))
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        print("##############################################")

    def __LevelUp(self):
        self.NewAction()
        self.__level += 1
        print("Level Up! ->"+str(self.__level))
        self.__nextExp *= self.__level * 2.5
        self.__maxHP += 50
        if self.exp >= self.__nextExp:            
            print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
            self.__LevelUp()

    def __del__(self):
        self.NewAction()
        print(self.name+" was Removed")

    def AddExp(self, exp):
        self.NewAction()
        self.exp += exp
        print("+"+str(exp)+"EXP")
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        if self.exp >= self.__nextExp:
            self.__LevelUp()

    #def ReturnExpOnDeath(self):
    #    return self.__level * 10

    def Death(self):
        self.NewAction()
        print(self.name+" is Dead")
        self.__del__()

    def SubHP(self, val):
        self.NewAction()
        self.__actHP -= val
        print("HP decreased: "+str(val))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        if self.__actHP <= 0:
            #self.ReturnExpOnDeath()
            self.Death()
    

class Human(LivingThing):
    #__level   = 0
    #__maxHP = 0
    #__nextExp = 0
    __skillPoints = 0

    def __init__(self, name, maxHP, debug):      
        self.debug = debug
        self.__nextExp = 100
        self.__level = 0
        self.__maxHP = maxHP
        self.__actHP = maxHP
        super().__init__(name, maxHP, debug)       

    def __LevelUp(self):
        super().NewAction()
        self.__level += 1
        self.__skillPoints += 5
        print("Level Up! ->"+str(self.__level))
        print("Available Skillpoints:"+str(self.__skillPoints))
        self.__nextExp *= self.__level * 2.5
        self.__maxHP *= 1.5
        if self.exp >= self.__nextExp:            
            print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
            self.__LevelUp()
        
    def AddExp(self, exp):
        super().NewAction()
        self.exp += exp
        print("+"+str(exp)+"EXP")
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        if self.exp >= self.__nextExp:
            self.__LevelUp()
   
    def Show (self):
        super().NewAction()
        print("##############################################")
        print("Name: "+self.name+" Level: "+str(self.__level))
        print("Exp:"+str(self.exp)+"/"+str(self.__nextExp))
        print("HP:"+str(self.__actHP)+"/"+str(self.__maxHP))
        print("Available Skillpoints:"+str(self.__skillPoints))
        print("##############################################")

class Creature(LivingThing):
    def __init__(self, name, maxHP, debug):
        super().__init__(name, maxHP, debug=debug)