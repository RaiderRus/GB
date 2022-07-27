# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 5, 2, 3, 4, 1, 7] => [1, 5]


lst = [1, 5, 2, 3, 4, 1, 7]


def ascending_sequence(array):
    print(f'Source list: {array}')
    array.sort()
    res = [array[0], array[0]]
    for i in range(1, len(array)):
        if array[i] - array[i - 1] == 1 or array[i] - array[i - 1] == 0:
            last = array[i]
        else:
            break
        res[1] = last
    return res


print(f'Increasing sequence: {ascending_sequence(lst)}')
