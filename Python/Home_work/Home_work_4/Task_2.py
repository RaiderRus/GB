# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input("Insert natural number: "))


def mult_list(n):
    array = []
    for i in range(2, n):
        while n % i == 0:
            array.append(i)
            n = n / i
        if n == 1:
            break
    if len(array) == 0:
        print("The number is simple.")
    else:
        print(f"Simple multipliers of a number: \n{', '.join(map(str, array))}")


mult_list(n)
