from telegram import Update
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.shared import DB_PATH, error_message

def button(update: Update, context: CallbackContext) -> None:
    chat_id= update.effective_chat.id
    query = update.callback_query
    conn = create_connection(DB_PATH)
    if conn:
        query.edit_message_text(text=f"Eliminazione del libro selezionato...")
        cur = conn.cursor()
        cur.execute("DELETE FROM Market WHERE rowid=?", (query.data,))
        conn.commit()
        conn.close()
        context.bot.send_message(chat_id, "Libro eliminato.")
    else:
        query.edit_message_text(text=error_message)
