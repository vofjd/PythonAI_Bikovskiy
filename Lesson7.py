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



# class counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
#
#
#
# count = counter(5)
# for elem in count:
#     print(elem)
#
#
#
#
# print("-"*30)
# count = counter(5)
# print(count.__next__())
# print(count.__next__())
# print(next(count))
#
#



#list generator
# list_power_2 = [i **2 for i in range(1, 20, 1)]
# print(list_power_2)

# """генератори в пайтон це функція,
# що повертає ітератор, який під час ітерації повертає послідовність значень"""
#
#
#
# def raise_to_the_degrees(number):
#     i = 0
#     # for _ in range(max_degrees):
#     while True:
#         result = number ** i
#         yield  result
#         yield number ** i
#         i += 1
#         if result > 100 ** 20:
#             return
#         i += 1
#
#
#
#
#
# res = raise_to_the_degrees(2)
# print(res)
#
# for elem in res:
#     print(elem)











class Helper:
    def __init__(self, work):
        self.work = work


    def __call__(self, work):
        return f"I will help you with your {self.work}. Afterwarsd I will help you with {work}"



hepler = Helper("homework")
print(hepler("cleaning"))
