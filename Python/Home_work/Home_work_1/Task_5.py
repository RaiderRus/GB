# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# *Пример:*
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


print('Insert coordinates: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'Distance between points A({x1},{y1}) and B({x2},{y2}) is {round(distance, 2)}')
