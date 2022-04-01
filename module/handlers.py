from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from module.start import start
from module.help import help
from module.search import search
from module.sell import sell
from module.delete import delete
from module.button import button


def handlers(updater: Updater) -> None:
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("vendi", sell))
    dispatcher.add_handler(CommandHandler("cerca", search))
    dispatcher.add_handler(CommandHandler("elimina", delete))
    dispatcher.add_handler(CallbackQueryHandler(button))
