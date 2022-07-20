# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


array = ["aaa", "bbb", "qqwe", "!!!!", "5", "290490"]
digits = []


def fill_array(array):
    for element in array:
        if element.isdigit():
            digits.append(int(element))


def print_array(digits):
    if len(digits) > 0:
        if len(digits) == 1:
            print(f"В заданном списке присутствует число {', '.join(map(str, digits))}.")
        else:
            print(f"В заданном списке присутствуют числа {', '.join(map(str, digits))}.")
    else:
        print("В заданном списке отсутствуют числа.")


fill_array(array)
print_array(digits)
