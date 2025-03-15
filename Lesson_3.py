class Human():
    def __init__(self, name="Human"):
        self.name = name



class Auto():
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []



    def add_passenger(self, human):
        self.passengers.append(human)



    def passengers_names(self):
        if self.passengers !=[]:
            print(f"Names of {self.brand} passengers:")
        for passenger in self.passengers:
            print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")


nick = Human("Nick")
kate = Human("Kate")
illia = Human("Illia")
denis = Human("Denis")
ann = Human("Ann")

car = Auto("Mersedes")
car2 = Auto("BMW")
car.add_passenger(nick)
car.add_passenger(kate)
car.passengers_names()

car2.add_passenger(illia)
car2.add_passenger(denis)
car2.add_passenger(ann)
car2.passengers_names()
