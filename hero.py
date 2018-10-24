class Hero():
    """ Class to create HERO for uor Game"""
    def __init__(self, name, level, race):
        """"initiate uor hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """" Print all parameters of this hero"""
        description = (self.name + " Level is: " + str(self.level) + " RACE is: " + self.race + " Health is " + str(self.health).title())
        print(description)

    def level_up(self):
        """ UPGRADE LEVEL"""
        self.level +=1

    def move(self):
        """ Start moving hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health

class SuperHero(Hero):
    """ Class to create superhero"""
    def __init__(self, name, level, race, magiclevel):
        """initiate superhero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.__magic = 100
# __magic запрещение изменениыя напрямую
    def makemagic(self):
        """ User magic"""
        self.__magic -= 10

    def show_hero(self):
        description = (self.name + " Level is: " + str(self.level) + " RACE is: " + self.race + " Health is " + str(
            self.health) + " Magic is : " + str(self.__magic).title())
        print(description)



