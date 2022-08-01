# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def rle_vhod():
    with open('text_data.txt') as file:
        data = list(map(str.strip, file.readlines()))

        result = []
    for line in data:
        simboll = ''
        count = 1
        c_ish = line[0]
        for i in range(1, len(line)):
            new_c = line[i]
            if new_c == c_ish:
                count += 1
            else:
                simboll += c_ish if count == 1 else str(count) + c_ish
                c_ish = line[i]
                count = 1
        simboll += c_ish if count == 1 else str(count) + c_ish
        result.append(simboll)
    with open('text_data.txt', 'w') as file:
        for line in result:
            print(line, file=file)
    return result


def rle_vihod():
    with open('text_data.txt') as file:
        data = list(map(str.strip, file.readlines()))
    result = []
    for line in data:
        simboll = ''
        n = ''
        for c_ish in line:
            if c_ish.isdigit():
                n += c_ish
            else:
                simboll += c_ish if n == '' else int(n) * c_ish
                n = ''
        result.append(simboll)
    with open('output_data.txt', 'w') as file:
        for line in result:
            print(line, file=file)
    return result


print('Сжатые данные :')
print(*rle_vhod())

print('Восстановленные данные :')
print(*rle_vihod())
