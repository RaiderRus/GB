# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Это не просто сумма всех коэффициентов.
# Сумма многочленов равна многочлену, членами которого являются все члены данных многочленов.
# Например, в 1 файле было 3*x^3 + 5*x^2+10*x+11, в другом 7*x^2+55
# то в итоге будет, 3*x^3 + 12*x^2+10*x+66


def open_and_modify(path):
    with open(path, 'r') as data:
        for line in data:
            s = line.replace(' ', '').replace(
                '+', ' +').replace('-', ' -').replace('=', ' =').strip().lower()
            lst = s.split(' ')
    return lst


def find_max_deg(lst):
    max_j = 0
    for i in range(0, len(lst)):
        if len(lst[i]) >= 3:
            str_x = str(lst[i])
            for j in range(2, 10):
                if f'x^{j}' == str_x[-3:] and max_j < j:
                    max_j = j
    return max_j


def polynomial_addition(lst1, lst2, max_deg):
    lst = []
    for i in range(max_deg, -1, -1):
        coef1 = 0
        coef2 = 0

        for j in range(len(lst1) - 1):
            s1 = str(lst1[j])

            if i == 0:
                if s1[-1] != 'x' \
                        and s1[-3] != 'x':
                    coef1 = int(s1)
            elif i == 1:
                if s1[-1] == 'x':
                    coef1 = int(s1[0:-1])
            else:
                if s1[-3:] == f'x^{i}':
                    coef1 = int(s1[0:-3])

        for j in range(len(lst2) - 1):
            s2 = str(lst2[j])

            if i == 0:
                if s2[-1] != 'x' \
                        and s2[-3] != 'x':
                    coef2 = int(s2)
            elif i == 1:
                if s2[-1] == 'x':
                    coef2 = int(s2[0:-1])
            else:
                if s2[-3:] == f'x^{i}':
                    coef2 = int(s2[0:-3])

        coef = coef1 + coef2

        if coef < 0:
            if i == 0:
                lst.append(coef)
            elif i == 1:
                lst.append(f'{coef}x')
            else:
                lst.append(f'{coef}x^{i}')

        if coef > 0:
            if i == 0:
                lst.append(f'+{coef}')
            elif i == 1:
                lst.append(f'+{coef}x')
            else:
                lst.append(f'+{coef}x^{i}')

    lst.append('=0')

    return lst


def clean_look(lst):
    lst_new = []
    for i in lst:
        i = str(i).replace('+', ' + ').replace('-', ' - ').replace('=', ' = ').strip()
        lst_new.append(i)
    return lst_new


path1 = 'file_1.txt'
path2 = 'file_2.txt'
l1 = open_and_modify(path1)
l2 = open_and_modify(path2)

max_deg = find_max_deg(l1) if find_max_deg(l1) > find_max_deg(l2) else find_max_deg(l2)

lst_res = polynomial_addition(l1, l2, max_deg)
f = open("sum_file.txt", 'w')
f.writelines(lst_res)
f.close()

print(*(clean_look(l1)))
print(*(clean_look(l2)))
print()
print(*(clean_look(lst_res)))
