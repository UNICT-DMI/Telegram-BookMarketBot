from telegram import Update
from telegram.ext import CallbackContext
from module.find import find
from module.create_connection import create_connection
from module.shared import DB_PATH

def search(update: Update, context: CallbackContext) -> None:
    chat_id=update.effective_chat.id
    message=update.message.text
    if message!='/cerca':
        message = message.split('/cerca ')[1]
        conn = create_connection(DB_PATH)
        if conn:
            rows = find(message, conn, 'Market')
            if len(rows):
                context.bot.send_message(chat_id, 'La ricerca ha prodotto i seguenti risultati:\n')
                for i in range(len(rows)):
                    res = 'n°: ' + str(i+1) + '\n' + 'ISBN: ' + rows[i][1] + '\n' + 'Titolo: ' + rows[i][2] + '\n' + 'Autori: '+ rows[i][3]+ '\n' + 'Venditore: ' + rows[i][4] + '\n' + 'Prezzo: ' + rows[i][5] + ' €\n'
                    context.bot.send_message(chat_id, res)
            else:
                context.bot.send_message(chat_id, "Non ho trovato nulla.")
        else:
            context.bot.send_message(chat_id, "Si è verificato un problema nella lettura del database.")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /cerca <txt>")
