import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import strings as st
import bot_token


def isWin(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False


def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == st.SYMBOL_UNDEF:
            counter += 1
    return counter


def game(callBackData):
    message = st.ANSW_YOUR_TURN  # сообщение, которое вернется
    alert = None

    buttonNumber = int(callBackData[0])  # считывание нажатой кнопки, преобразуя ее из строки в число
    if not buttonNumber == 9:  # цифра 9 передается в первый раз в качестве заглушки. Т.е. если передана цифра 9, то клавиатура для сообщения создается впервые
        charList = list(callBackData)  # строчка callBackData разбивается на посимвольный список "123" -> ['1', '2', '3']
        charList.pop(0)  # удаление из списка первого элемента: который отвечает за выбор кнопки
        if charList[buttonNumber] == st.SYMBOL_UNDEF:  # проверка: если в нажатой кнопке не выбран крестик/нолик, то можно туда сходить крестику
            charList[buttonNumber] = st.SYMBOL_X  # эмуляция хода крестика
            if isWin(charList, st.SYMBOL_X):  # проверка: выиграл ли крестик после своего хода
                message = st.ANSW_YOU_WIN
            else:  # если крестик не выиграл, то может сходит бот, т.е. нолик
                if countUndefinedCells(charList) != 0:  # проверка: есть ли свободные ячейки для хода
                    # если есть, то ходит бот (нолик)
                    isCycleContinue = True
                    # запуск бесконечного цикла т.к. необходимо, чтобы бот походил в свободную клетку, а клетка выбирается случайным образом
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  # генерация случайного числа - клетки, в которую сходит бот
                        if charList[rand] == st.SYMBOL_UNDEF:  # если клетка неопределенна, то ходит бот
                            charList[rand] = st.SYMBOL_O
                            isCycleContinue = False  # смена значения переменной для остановки цикла
                            if isWin(charList, st.SYMBOL_O):  # проверка: выиграл ли бот после своего кода
                                message = st.ANSW_BOT_WIN

        # если клетка, в которую хотел походить пользователь уже занята:
        else:
            alert = st.ALERT_CANNOT_MOVE_TO_THIS_CELL

        # проверка: остались ли свободные ячейки для хода и что изначальное сообщение не поменялось (означает, что победителя нет, и что это был не ошибочный ход)
        if countUndefinedCells(charList) == 0 and message == st.ANSW_YOUR_TURN:
            message = st.ANSW_DRAW

        # формирование новой строчки callBackData на основе сделанного хода
        callBackData = ''
        for c in charList:
            callBackData += c

    # проверка, что игра закончилась (message равно одному из трех вариантов: победил Х, 0 или ничья):
    if message == st.ANSW_YOU_WIN or message == st.ANSW_BOT_WIN or message == st.ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  # обнуление callBackData

    return message, callBackData, alert


def getKeyboard(callBackData):
    keyboard = [[], [], []]  # заготовка объекта клавиатуры, которая вернется

    if callBackData != None:  # если
        # формирование объекта клавиатуры
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))

    return keyboard


def newGame(update, _):
    data = ''
    for i in range(0, 9):
        data += st.SYMBOL_UNDEF
    update.message.reply_text(st.ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))


def button(update, _):
    query = update.callback_query
    callbackData = query.data  # получение callbackData, скрытых в кнопке

    message, callbackData, alert = game(callbackData)  # игра
    if alert is None:  # если не получен сигнал тревоги (alert==None), то редактируем сообщение и меняем клавиатуру
        query.answer()  # обязательно нужно что-то отправить в ответ, иначе могут возникнуть проблемы с ботом
        query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(getKeyboard(callbackData)))
    else:  # если получен сигнал тревоги (alert!=None), то отобразить сообщение о тревоге
        query.answer(text=alert, show_alert=True)


def help_command(update, _):
    update.message.reply_text(st.ANSW_HELP)


if __name__ == '__main__':
    updater = Updater(bot_token.token)  # получения токена

    # добавление обработчиков
    updater.dispatcher.add_handler(CommandHandler('start', newGame))
    updater.dispatcher.add_handler(CommandHandler('new_game', newGame))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, help_command))  # обработчик на любое текстовое сообщение
    updater.dispatcher.add_handler(CallbackQueryHandler(button))  # добавление обработчика на CallBack кнопки

    # Запуск бота
    updater.start_polling()
    print("start server")
    updater.idle()
