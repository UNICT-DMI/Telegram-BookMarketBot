from telegram import Update
from telegram.ext import CallbackContext
from module.find import find
from module.create_connection import create_connection
from module.send_results import send_results
from module.shared import DB_PATH, error_message


def search(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message == "/cerca":
        context.bot.send_message(chat_id, "Utilizzo comando: /cerca <txt>")
        return

    message = message.split("/cerca ")[1]
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, error_message)
        return

    rows = find(message, conn, "Market")
    conn.close()
    if rows:
        context.bot.send_message(
            chat_id, "La ricerca ha prodotto i seguenti risultati:\n"
        )
        send_results(rows, chat_id, context)
    else:
        context.bot.send_message(chat_id, "Non ho trovato nulla.")
