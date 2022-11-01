from telegram import Update
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.shared import DB_PATH


def button(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query
    conn = create_connection(DB_PATH)
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM Market WHERE rowid=?", (query.data,))
        query.edit_message_text(text="Eliminazione del libro selezionato...")
        conn.commit()
        context.bot.send_message(chat_id, "Libro eliminato.")
    else:
        query.edit_message_text(text="Si è verificato un problema nella lettura del database.")
