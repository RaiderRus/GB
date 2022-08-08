# модуль для взаимодейсвия с пользователем - ввод выражения в виде строки

def get_value():
    expresion = ''
    for element in input('Введите выражение: '):
        expresion += str(element)
    return expresion
