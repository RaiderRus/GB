from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import bot_token
import tic_tac_toe


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Приветики, пистолетики! {update.effective_user.first_name}!')


def UserMessage(update: Update, context: CallbackContext):
    if(update.message.text == "Кто ты?"):
        update.message.reply_text("Бот Райдера")
    else:
        try:
            update.message.reply_text(eval(update.message.text))
        except:
            update.message.reply_text("Не понятно")


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""Мои команды:
    /start
    /hello
    /game
    """)


def stop(update: Update, context: CallbackContext) -> None:
    updater.stop()


def game(update: Update, context: CallbackContext) -> None:
    tic_tac_toe.start_game()


updater = Updater(bot_token.token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('game', game))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))
print('server start')
updater.start_polling()
updater.idle()
