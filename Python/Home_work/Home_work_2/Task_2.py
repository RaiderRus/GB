# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(num, arr_num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
        arr_num.append(f)
    print(arr_num)


number = int(input("Insert number: > "))
array_number = []

factorial(number, array_number)
