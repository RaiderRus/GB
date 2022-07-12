# 4- Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input('Insert the number of the quarter of the coordinate plane: '))
if number_quarter == 1:
    print(f'In {number_quarter} quarter range: x > 0, y > 0')
elif number_quarter == 2:
    print(f'In {number_quarter} quarter range: x < 0, y > 0')
elif number_quarter == 3:
    print(f'In {number_quarter} quarter range: x < 0, y < 0')
elif number_quarter == 4:
    print(f'In {number_quarter} quarter range: x > 0, y < 0')
else:
    print('Input error')
