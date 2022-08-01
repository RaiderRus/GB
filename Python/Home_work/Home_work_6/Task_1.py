# Создайте программу для игры в "Крестики-нолики".


from random import randint

field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
count = randint(1, 3)


def print_field(field):
    for i in range(0, len(field)):
        for i2 in range(0, len(field[i])):
            print(field[i][i2], end=' ')
        print()


def win_chek(field):
    if field[0][0] == field[0][1] == field[0][2] != '_' or field[0][0] == field[1][1] == field[2][2] != '_' or field[0][
        0] == \
            field[1][0] == field[2][0] != '_' or field[0][0] == field[1][0] == field[2][0] != '_' or field[0][2] == \
            field[1][
                2] == field[2][2] != '_' or field[0][0] == field[1][1] == field[2][2] != '_' or field[0][2] == field[1][
        1] == field[2][
        0] != '_' or field[2][0] == field[2][1] == field[2][2] != '_' or field[0][0] == field[1][0] == field[2][
        0] != '_' or \
            field[0][2] == field[1][2] == field[2][2] != '_' or field[0][0] == field[1][1] == field[2][2] != '_' or \
            field[0][
                2] == field[1][1] == field[2][0] != '_' or field[0][1] == field[1][1] == field[2][1] != '_':
        return True
    else:
        return False


def opponent(field):
    x = randint(0, 2)
    y = randint(0, 2)
    while field[x][y] != '_':
        x = randint(0, 2)
        y = randint(0, 2)
    print(f'The opponent goes to {x + 1}, {y + 1}')
    field[x][y] = 'O'
    print('The opponent\'s move is accepted')


def player(field):
    x = int(input('Insert the line number: '))
    y = int(input('Insert the column number: '))
    x -= 1
    y -= 1
    print(f'Player goes to {x + 1}, {y + 1}')
    while field[x][y] != '_':
        x = int(input('The field is already occupied, re-insert the line number: ')) + 1
        y = int(input('Insert the column number: ')) + 1
        print(f'Player goes to {x + 1}, {y + 1}')
    field[x][y] = 'X'
    print('The player\'s move is accepted')


def draw_check(field):
    empty = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if field[i][j] == '_':
                empty = +1
    if empty == 0:
        return True
    else:
        return False


print(f'count={count}')
print('The game begins')
if count % 2 == 0:
    print('The player goes first')
else:
    print('The bot goes first')
print_field(field)

while win_chek(field) != True:
    if count % 2 == 0:
        player(field)
        print_field(field)
        count += 1
        if win_chek(field) == True:
            print('The game is over! The player won')
            break
    else:
        opponent(field)
        print_field(field)
        count += 1
        if win_chek(field) == True:
            print('The game is over! The bot won')
    if draw_check(field) == True:
        print('Game over, draw')
        break
