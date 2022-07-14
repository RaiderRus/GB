# 3- Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# *Пример:*
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def Quarter_Search(x, y):
    if x > 0 and y > 0:
        print(f'Point ({x}; {y}) is in 1 quarter')
    if x < 0 and y > 0:
        print(f'Point ({x}; {y}) is in 2 quarter')
    if x < 0 and y < 0:
        print(f'Point ({x}; {y}) is in 3 quarter')
    if x > 0 and y < 0:
        print(f'Point ({x}; {y}) is in 4 quarter')
    if x == 0 or y == 0:
        print('Insert numbers other than 0')

x = float(input('Insert coordinates x = '))
y = float(input('Insert coordinates y = '))
Quarter_Search(x, y)
