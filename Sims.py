import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        if self.satiety >= 100:
            self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return

        if manage == "fuel":
            if self.money >= 100:
                print("I bought fuel")
                self.money -= 100
                self.car.fuel += 100
        elif manage == 'food':
            if self.money >= 50:
                print("I bought food")
                self.money -= 50
                self.home.food += 50
        elif manage == "delicacies":
            if self.money >= 15:
                print("Hooray! Delicious!")
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        if self.money >= 50:
            print("Repairing the car...")
            self.car.strength += 100
            self.money -= 50
        else:
            print("Not enough money for repairs!")

    def days_indexes(self, day):
        print("{:^50}".format(f" Today is day {day} of {self.name}'s life "))
        print(f"Money: {self.money} | Satiety: {self.satiety} | Gladness: {self.gladness}")
        print(f"Food: {self.home.food} | Mess: {self.home.mess}")
        print(f"Car ({self.car.brand}) - Fuel: {self.car.fuel} | Strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            # noinspection PyUnresolvedReferences
            print(f"I bought a car: {self.car.brand}")
        if self.job is None:
            self.get_job()
            # noinspection PyUnresolvedReferences
            print(f"I got a job: {self.job} with a salary of {self.job.salary}")

        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there's too much mess… Cleaning instead!")
                self.clean_home()
            else:
                print("Let's chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        print("The car cannot move")
        return False


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, jobs_list):
        self.job = random.choice(list(jobs_list))
        self.salary = jobs_list[self.job]['salary']
        self.gladness_less = jobs_list[self.job]['gladness_less']


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}