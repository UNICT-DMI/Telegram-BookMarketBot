from telegram import Update
from telegram.ext import CallbackContext
from module.find import find
from module.send_results import send_results
from module.shared import SEARCH_USAGE, MARKET, NOTHING_FOUND, SEARCH_RESULT


def search(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message == "/cerca":
        context.bot.send_message(chat_id, SEARCH_USAGE)
        return

    _, message = message.split("/cerca ")
    rows = find(context, chat_id, message, MARKET)

    if rows:
        context.bot.send_message(chat_id, SEARCH_RESULT)
        send_results(rows, chat_id, context)
    else:
        context.bot.send_message(chat_id, NOTHING_FOUND)
