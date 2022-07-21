# Вычислить результат деления двух чисел c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


num_1 = float(input('Insert first number: '))
num_2 = float(input('Insert second number: '))
d = float(input('Set the division accuracy: '))


def my_round(a, b, c):
    if 10 ** (-1) >= c >= 10 ** (-10):
        res = a / b
        osn = 1
        while c < 0.1:
            c *= 10
            osn += 1
        res = round(res, osn)
        return res
    else:
        return 'd must be 0,1 >= d >= 0.0000000001'


print(my_round(num_1, num_2, d))
