# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 67,82 -> 23
# - 0,56 -> 11


def print_sum_numbers(num):
    sum_numbers = 0
    str_number = str(num)
    for i in str_number:
        if i == ".":
            continue
        sum_numbers = int(sum_numbers) + int(i)
    print(f'Sum numbers is {sum_numbers}')


number = float(input('Insert float number: > '))
number = abs(number)

print_sum_numbers(number)
