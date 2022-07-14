# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(num):
    array_number = []
    f = 1
    for i in range(1, num + 1):
        f = f * i
        array_number.append(f)
    print(array_number)


number = int(input("Insert number: > "))

factorial(number)
