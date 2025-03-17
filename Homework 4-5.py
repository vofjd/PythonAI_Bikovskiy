class Hamster:
    def __init__(self, name = "Hamster"):
        self.name = name
        self.money = 20
        self.gladness = 15
        self.satiety = 10
        self.food = 0



        print(f"Names of hamster - {self.name}")
        print(f" Money of hamster {self.money}")
        print(f"  Gladness of hamster {self.gladness}")
        print(f"   Satiety of hamster {self.satiety}")
        print(f"    Food of hamster {self.food}")
        print("-----------------------------------")




    def eat_pizza(self):
        if self.gladness >= 50:
            print("--------Eating_Pizza--------")
            self.satiety +=5
            self.food -= 3
            print(f"Names of hamster - {self.name}")
            print(f" Money of hamster {self.money}")
            print(f"  Gladness of hamster {self.gladness}")
            print(f"   Satiety of hamster {self.satiety}")
            print(f"    Food of hamster {self.food}")
            print("-----------------------------------")

    def get_money(self):
     if self.money >= 50:
        print("--------Getting_Money--------")
        self.money += 30
        self.gladness -= 3
        self.satiety -= 4
        print(f"Names of hamster - {self.name}")
        print(f" Money of hamster {self.money}")
        print(f"  Gladness of hamster {self.gladness}")
        print(f"   Satiety of hamster {self.satiety}")
        print(f"    Food of hamster {self.food}")
        print("-----------------------------------")


    def buy_pizza(self):
        if self.food == 0:
            print("--------Buying_Pizza--------")
            self.money -= 50
            self.gladness += 10
            self.satiety += 2
            print(f"Names of hamster - {self.name}")
            print(f" Money of hamster {self.money}")
            print(f"  Gladness of hamster {self.gladness}")
            print(f"   Satiety of hamster {self.satiety}")
            print(f"    Food of hamster {self.food}")
            print("-----------------------------------")

    def chill(self):
     if self.gladness >= 30:
        print("--------Chilling--------")
        self.gladness += 10
        print(f"Names of hamster - {self.name}")
        print(f" Money of hamster {self.money}")
        print(f"  Gladness of hamster {self.gladness}")
        print(f"   Satiety of hamster {self.satiety}")
        print(f"    Food of hamster {self.food}")
        print("-----------------------------------")






mr_teacake = Hamster("mr_Teacake")
mr_potcake = Hamster("mr_Potcake")
mr_badil = Hamster("mr_Badil")