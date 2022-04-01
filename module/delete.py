from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.send_results import send_results
from module.shared import DB_PATH, error_message

def delete(update: Update, context: CallbackContext) -> None:
    chat_id= update.effective_chat.id
    message=update.message.text
    if message =='/elimina':
        user ="@"+str(context.bot.get_chat(chat_id)['username'])
        conn = create_connection(DB_PATH)
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT rowid, * FROM Market WHERE Venditore=?", (user,))
            rows = cur.fetchall()
            conn.close()
            if rows:
                context.bot.send_message(chat_id, "Hai i seguenti libri in vendita:\n")
                send_results(rows, chat_id, context)
                keyboard = [ [InlineKeyboardButton(str(i+1), callback_data=(rows[i][0]))] for i in range(len(rows))]
                reply_markup = InlineKeyboardMarkup(keyboard)
                update.message.reply_text('Quale libro vuoi eliminare?', reply_markup=reply_markup)
            else:
                context.bot.send_message(chat_id, "Non hai nessun libro in vendita.")
        else:
            context.bot.send_message(chat_id, error_message)
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /elimina")
