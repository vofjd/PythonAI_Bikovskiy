def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)


def write():
    input_list = []
    while True:
        element = input("Введіть елементи списку ")
        input_list.append(element)
        return input_list

lst = write()
process_list(lst)











