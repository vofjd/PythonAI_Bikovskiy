#print(10/0)
#print("Програма продовжує працювати")
# try:
#     print(10/0)
# except(ZeroDivisionError):
#     print("Не можливо ділити на 0")
#
# print("Програма продовжує працювати")


# class BuildingError(Exception):
#     def __init__(self, val):
#         self.val = val
#     def __str__(self):
#         return f"З такою кількістю матеріалів {self.val} неможливо побудувати будинок"
#
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Достатньо матеріалів"
#     else:
#         raise BuildingError(amount_of_material)
#
#
# material = 123
#
# try:
#     print(check_material(material, 300))
# except BuildingError as e:
#     print(e)



# try:
#     numerator = int(input("Введіть чисельник"))
#     denominator = int(input("введіть знаменник"))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка : Ділення на 0 не можливо")
# except ValueError:
#     print("Помилка : Введені данні не є числом")
#



import warnings
from logging import warning
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Putin huylo", SyntaxWarning)


try:
    warnings.warn("Warning, module not import", ImportWarning)
except:
    print("Warning")






















