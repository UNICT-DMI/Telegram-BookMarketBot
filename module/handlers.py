from telegram.ext import CommandHandler, CallbackQueryHandler
from module.start import start
from module.help import help
from module.vendi import vendi
from module.cerca import cerca
from module.elimina import elimina
from module.button import button

def handlers(updater):
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('vendi', vendi))
    dispatcher.add_handler(CommandHandler('cerca', cerca))
    dispatcher.add_handler(CommandHandler('elimina', elimina))
    dispatcher.add_handler(CallbackQueryHandler(button))