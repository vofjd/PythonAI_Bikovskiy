# class Human():
#     height = 180
#
# class Student(Human):
#     satiety = 0
#
# class Worker(Human):
#     satiety = 100
#
# h = Human()
# s = Student()
# w = Worker()
#
#
#
# print(h.height)
# print("*"*20)
# print(s.satiety)
# print(s.height)
# print("*"*20)
# print(w.satiety)
# print(w.height)

print("-------------------------------------------------")

class Grandparent():
    height = 170
    satiety = 100
    age = 60


class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(f"height = {self.height}")
        print(f"satiety = {self.satiety}")
        print(f"age = {self.age}")
nich = Child()

print("-------------------------------------------------")

class Hello():
    def __init__(self):
        print("Hello")


class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print("World")




hw = HelloWorld()

print("-------------------------------------------------")














class Computer:
    def __init__(self, model):
        self.model = model
        self.memory = 128

    def calculate(self):
        print("Calculating...")

class Monitor:
    def __init__(self):
        self.resolution = '4k'

    def display(self):
        print("I show the image on the screen")

class Monoblock(Computer, Monitor):
    def __init__(self, model):
        Computer.__init__(self, model)
        Monitor.__init__(self)

    def print_info(self):
        self.display()
        self.calculate()
        print(f"Model: {self.model}")
        print(f"Resolution: {self.resolution}")
        print(f"Memory: {self.memory} GB")

mb = Monoblock(model="Last")
mb.print_info()

print("-------------------------------------------------")