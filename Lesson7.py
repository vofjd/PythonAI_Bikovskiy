# import random
# my_list = []
#
#
# for i in range(10):
#     my_list.append(random.randint(-10, 10))
#
# print(my_list)
# print("-"*20)
#
#
#
# iterator = iter(my_list)
# print(iterator)
#
#
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #print(next(iterator))
#
# print("-"*20)
#
#
# iterator = iter(my_list)
#
#
# for elem in iterator:
#     print(elem)
from collections import Counter


class counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i




count = counter(5)
for elem in count:
    print(elem)




print("-"*30)
count = counter(5)
print(count.__next__())
print(count.__next__())
print(next(count))


