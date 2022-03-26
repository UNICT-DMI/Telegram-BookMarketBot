from module.get_on_sale import get_on_sale
from module.find_book import find_book
from telegram import Update
from telegram.ext import CallbackContext

def search(update: Update, context: CallbackContext) -> None:
    chat_id=update.effective_chat.id
    message=update.message.text
    if message!='/cerca':
        message = message.split('/cerca ')[1]
        df = get_on_sale()
        found, v = find_book(message, df)
        if found:
            res='La ricerca ha prodotto i seguenti risultati:\n\n'
            for i in range(len(v)):
                res+='ISBN: ' +str(df.iloc[v[i]][0]) + '\n' + 'Titolo: ' +str(df.iloc[v[i]][1]) + '\n' + 'Autori: '+str(df.iloc[v[i]][2]) + '\n' + 'Venditore: ' + str(df.iloc[v[i]][3]) + '\n' + 'Prezzo: ' + str(df.iloc[v[i]][4]) + ' €\n\n'
            context.bot.send_message(chat_id, res)
        else:
            context.bot.send_message(chat_id, "Non ho trovato nulla.")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /cerca <txt>")
