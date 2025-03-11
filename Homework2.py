class Cat:
    weight = 150
    print("-----------Lifecycle of the cat-----------")
    print()
    def __init__(self, name=None, feed = 20):
        self.name = name
        self.height = 50
        print("HiMeow!  ^_^")
        Cat.weight +=1
        self.feed = feed


    def __str__(self):
        return f"I am a Cat. My name is {self.name} ^_^"

    def add_feed(self):
        self.feed += 50




print("----Marshmallow----")
Marshmallow = Cat(name = "Marshmallow",feed = 100)
print(Marshmallow)
Marshmallow.add_feed()
print(f"My Weight is",Marshmallow.weight)
print(f"My Height is",Marshmallow.height)
print(f"feed for Marshmallow - {Marshmallow.feed} ^_^")
