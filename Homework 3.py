class Hamster:
    def __init__(self, name="Hamster"):
        self.name = name
        self.money = 20
        self.gladness = 15
        self.satiety = 10
        self.food = 0
        self.status()

    def status(self):
        print(f"Name: {self.name}")
        print(f" Money: {self.money}")
        print(f" Gladness: {self.gladness}")
        print(f" Satiety: {self.satiety}")
        print(f" Food: {self.food}")
        print("-----------------------------------")

    def eat_pizza(self):
        print("--------Eating Pizza--------")
        if self.food >= 3:
            self.satiety += 5
            self.food -= 3
        else:
            print("Not enough food!")
        self.status()

    def get_money(self):
        print("--------Getting Money--------")
        self.money += 30
        self.gladness -= 3
        self.satiety -= 4
        self.status()

    def buy_pizza(self):
        print("--------Buying Pizza--------")
        if self.money >= 50:
            self.money -= 50
            self.gladness += 10
            self.satiety += 2
            self.food += 3
        else:
            print("No money!")
        self.status()

    def chill(self):
        print("--------Chilling--------")
        self.gladness += 10
        self.status()


def live_hamster(hamster):
    if hamster.gladness >= 50:
        hamster.eat_pizza()
    if hamster.money < 50:
        hamster.get_money()
    if hamster.food == 0 and hamster.money >= 50:
        hamster.buy_pizza()
    if hamster.gladness >= 30:
        hamster.chill()



mr_teacake = Hamster("mr_Teacake")
mr_potcake = Hamster("mr_Potcake")
mr_badil = Hamster("mr_Badil")


for _ in range(3):
    live_hamster(mr_teacake)
    live_hamster(mr_potcake)
    live_hamster(mr_badil)
print("We are happy!")