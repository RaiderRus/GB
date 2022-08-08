# модуль для вычисления выражений с комплексными числами

# разбивает строку на список из чисел и арифметических операций
def list_of_numbers_and_operations(new_string):
    list_of_numbers = []
    num = ''
    for i in range(len(new_string)):
        if new_string[i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'j']:
            num += new_string[i]
            if i == len(new_string) - 1:
                list_of_numbers.append(num)
        elif new_string[i] in ['*', '/', '+', '-', '^']:
            if new_string[i-1] not in [')']:
                list_of_numbers.append(num)
            list_of_numbers.append(new_string[i])
            num =''
        elif new_string[i] in ['(']:
            list_of_numbers.append(new_string[i])
            num =''
        elif new_string[i] in [')']:
            list_of_numbers.append(num)
            list_of_numbers.append(new_string[i])
    # print(list_of_numbers)
    return list_of_numbers

# выполняет арифметические операции с учетом приоритета, сокращает список, заменяя выполненное выражение на результат
def calculation(list_of_numbers):
    while '^' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "^":
                result = complex(list_of_numbers[i-1]) ** complex(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '/' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "/":
                result = complex(list_of_numbers[i-1]) / complex(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '*' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "*":
                result = complex(list_of_numbers[i-1]) * complex(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    while '-' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "-":
                try:
                    result = complex(list_of_numbers[i-1]) - complex(list_of_numbers[i+1])
                    list_of_numbers[i-1] = result
                    list_of_numbers.pop(i+1)
                    list_of_numbers.pop(i)
                    break
                except ValueError:
                    result = 0 - float(list_of_numbers[i + 1])
                    list_of_numbers[i - 1] = result
                    list_of_numbers.pop(i + 1)
                    list_of_numbers.pop(i)
                    break
    while '+' in list_of_numbers:
        for i in range(len(list_of_numbers)):
            if (list_of_numbers[i]) == "+":
                result = complex(list_of_numbers[i-1]) + complex(list_of_numbers[i+1])
                list_of_numbers[i-1] = result
                list_of_numbers.pop(i+1)
                list_of_numbers.pop(i)
                break
    result = list_of_numbers[0]
    return result

# выполняет выражения в скобках, сокращает список, заменяя выполненное выражение на результат
# далее считает выражение без скобок
def parentheses(list_of_numbers):
    while '(' in list_of_numbers or ')' in list_of_numbers:
        begin = 0
        end = len(list_of_numbers)
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == '(':
                begin = i + 1
                # print(begin)
            if list_of_numbers[i] == ')':
                end = i
                # print(end)
                list_in_parenthese = []
                for j in range(begin, end):
                    list_in_parenthese.append(list_of_numbers[j])
                # print(list_in_parenthese)
                result = calculation(list_in_parenthese)
                # print(result)
                list_of_numbers[begin - 1] = result
                del list_of_numbers[begin: end + 1]
                # print(list_of_numbers)
                break
    result = calculation(list_of_numbers)
    return result


# str_one = '(-12+3j)*(-2+4j)'
# numbers_one = list_of_numbers_and_operations(str_one)
# print(f'{str_one} => {parentheses(numbers_one)}')

# str_five2 = '(-12+3j)*(-2+4j)'
# print(f'С функцией eval: {str_five2} => {eval(str_five2)}')
