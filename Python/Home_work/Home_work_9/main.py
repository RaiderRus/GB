from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


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
    """)


updater = Updater('5432914197:AAFH7AdFeDUAdOtGII3D_R7Js2wjnww6-Rs')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))
print('server start')
updater.start_polling()
updater.idle()
