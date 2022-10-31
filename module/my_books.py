from typing import List
from telegram import Update
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.shared import DB_PATH, error_message
from module.send_results import send_results


def get_user_books(context: CallbackContext, chat_id: int) -> List[tuple]:
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, error_message)
        return

    user = "@" + str(context.bot.get_chat(chat_id)["username"])
    cur = conn.cursor()
    cur.execute("SELECT rowid, * FROM Market WHERE Seller=?", (user,))
    rows = cur.fetchall()
    conn.close()

    if rows:
        context.bot.send_message(chat_id, "Hai i seguenti libri in vendita:\n")
        send_results(rows, chat_id, context)
    else:
        context.bot.send_message(chat_id, "Non hai libri in vendita.")
    return rows


def my_books(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message != "/libri":
        context.bot.send_message(chat_id, "Utilizzo comando: /libri")
        return
    get_user_books(context, chat_id)
