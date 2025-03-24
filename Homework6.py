
result = []
def divider(a, b):
 if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Це не числа")
 if a < b:
    raise ValueError("Занадто маленьке число")
 if b > 100:
    raise IndexError("Занадто велике число")
 if b == 0:
     raise ZeroDivisionError("Не можна ділити на нуль")

 return a/b





data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        pass


print(result)