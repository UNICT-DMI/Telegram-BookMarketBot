from module.get_on_sale import get_on_sale
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def delete(update: Update, context: CallbackContext) -> None:
    chat_id= update.effective_chat.id
    message=update.message.text
    if message =='/elimina':
        user ="@"+str(context.bot.get_chat(chat_id)['username'])
        df = get_on_sale()
        ret = []
        for i in range(len(df)):
            if user == str(df['Venditore'][i]):
                ret.append(df.iloc[i].name)

        if len(ret)!=0:
            context.bot.send_message(chat_id, "Quale libro vuoi eliminare?\n")
            res=""
            for i in range(len(ret)):
                res+='n°: ' + str(i+1) + '\n' + 'ISBN: ' +str(df.iloc[ret[i]][0]) + '\n' + 'Titolo: ' +str(df.iloc[ret[i]][1]) + '\n' + 'Autori: '+str(df.iloc[ret[i]][2]) + '\n' + 'Venditore: ' + str(df.iloc[ret[i]][3]) + '\n' + 'Prezzo: ' + str(df.iloc[ret[i]][4]) + ' €\n\n' 
            keyboard = [ [InlineKeyboardButton(str(i+1), callback_data=(ret[i]))] for i in range(len(ret)) ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(res, reply_markup=reply_markup)
        else:
            context.bot.send_message(chat_id, "Non hai nessun libro in vendita")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /elimina")
