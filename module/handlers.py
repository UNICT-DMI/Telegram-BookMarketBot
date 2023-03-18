from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from module.start import start
from module.help import help # pylint: disable=redefined-builtin
from module.search import search
from module.sell import sell
from module.delete import delete
from module.my_books import my_books
from module.request import request
from module.stats import stats
from module.button import button


def handlers(updater: Updater) -> None:
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("vendi", sell))
    dispatcher.add_handler(CommandHandler("cerca", search))
    dispatcher.add_handler(CommandHandler("elimina", delete))
    dispatcher.add_handler(CommandHandler("libri", my_books))
    dispatcher.add_handler(CommandHandler("richiedi", request))
    dispatcher.add_handler(CommandHandler("stats", stats))
    dispatcher.add_handler(CallbackQueryHandler(button))
