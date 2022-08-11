# Создайте программу для игры в "Крестики-нолики".
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from random import randint


def start_game(update: Update, context: CallbackContext) -> None:
    field = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
    count = randint(1, 3)

    def print_field(field):
        for i in range(0, len(field)):
            for i2 in range(0, len(field[i])):
                update.message.reply_text(field[i][i2], end=' ')
            update.message.reply_text()

    def win_chek(field):
        if field[0][0] == field[0][1] == field[0][2] != '_' or field[0][0] == field[1][1] == field[2][2] != '_' or \
                field[0][
                    0] == \
                field[1][0] == field[2][0] != '_' or field[0][0] == field[1][0] == field[2][0] != '_' or field[0][2] == \
                field[1][
                    2] == field[2][2] != '_' or field[0][0] == field[1][1] == field[2][2] != '_' or field[0][2] == \
                field[1][
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
        update.message.reply_text(f'The opponent goes to {x + 1}, {y + 1}')
        field[x][y] = 'O'
        update.message.reply_text('The opponent\'s move is accepted')

    def player(field):
        x = int(input('Insert the line number: '))
        y = int(input('Insert the column number: '))
        x -= 1
        y -= 1
        update.message.reply_text(f'Player goes to {x + 1}, {y + 1}')
        while field[x][y] != '_':
            x = int(input('The field is already occupied, re-insert the line number: ')) + 1
            y = int(input('Insert the column number: ')) + 1
            update.message.reply_text(f'Player goes to {x + 1}, {y + 1}')
        field[x][y] = 'X'
        update.message.reply_text('The player\'s move is accepted')

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

    # print(f'count={count}')
    update.message.reply_text('The game begins')
    if count % 2 == 0:
        update.message.reply_text('The player goes first')
    else:
        update.message.reply_text('The bot goes first')
    print_field(field)

    while win_chek(field) != True:
        if count % 2 == 0:
            player(field)
            print_field(field)
            count += 1
            if win_chek(field) == True:
                update.message.reply_text('The game is over! The player won')
                break
        else:
            opponent(field)
            print_field(field)
            count += 1
            if win_chek(field) == True:
                update.message.reply_text('The game is over! The bot won')
        if draw_check(field) == True:
            update.message.reply_text('Game over, draw')
            break
