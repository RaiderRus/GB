# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_day_number = int(input('Enter the number of the day of the week: > '))
if 5 < week_day_number < 8:
    print('Yes')
elif 0 < week_day_number < 6:
    print('No')
else:
    print('Input error')
