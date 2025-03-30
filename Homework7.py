class Main:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        for i in range(self.start, self.end):
            yield i

print("-"*20)
iterable = Main(1, 5)

for num in iterable:
    print(num)
print("-"*20)
