from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.shared import DB_PATH

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
            if len(rows):
                context.bot.send_message(chat_id, "Hai i seguenti libri in vendita:\n")
                for i in range(len(rows)):
                    res = 'n°: ' + str(i+1) + '\n' + 'ISBN: ' + rows[i][1] + '\n' + 'Titolo: ' + rows[i][2] + '\n' + 'Autori: '+ rows[i][3] + '\n' + 'Venditore: ' + rows[i][4] + '\n' + 'Prezzo: ' + rows[i][5] + ' €\n'
                    context.bot.send_message(chat_id, res +'\n')
                keyboard = [ [InlineKeyboardButton(str(i+1), callback_data=(rows[i][0]))] for i in range(len(rows))]
                reply_markup = InlineKeyboardMarkup(keyboard)
                update.message.reply_text('Quale libro vuoi eliminare?', reply_markup=reply_markup)
            else:
                context.bot.send_message(chat_id, "Non hai nessun libro in vendita.")
        else:
            context.bot.send_message(chat_id, "Si è verificato un problema nella lettura del database.")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /elimina")
