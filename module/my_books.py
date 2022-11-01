from typing import List, Optional
from telegram import Update
from telegram.ext import CallbackContext
from module.create_connection import connect_and_execute, create_connection
from module.shared import DB_PATH,DB_ERROR,MY_BOOKS_USAGE,SELECT,LIST_BOOKS,NO_BOOKS
from module.send_results import send_results


# pylint: disable=inconsistent-return-statements
def get_user_books(context: CallbackContext, chat_id: int) -> Optional[List[tuple]]:
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, DB_ERROR)
        return

    user = "@" + str(context.bot.get_chat(chat_id)["username"])
    query = "SELECT rowid, * FROM Market WHERE Seller=?"
    rows = connect_and_execute(context, chat_id, query, (user,), SELECT)

    if rows:
        context.bot.send_message(chat_id, LIST_BOOKS)
        send_results(rows, chat_id, context)
    else:
        context.bot.send_message(chat_id, NO_BOOKS)
    return rows


def my_books(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message != "/libri":
        context.bot.send_message(chat_id, MY_BOOKS_USAGE)
        return
    get_user_books(context, chat_id)
