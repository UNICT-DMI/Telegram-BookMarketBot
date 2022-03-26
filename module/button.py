from module.get_on_sale import get_on_sale
from telegram import Update
from telegram.ext import CallbackContext

def button(update: Update, context: CallbackContext) -> None:
    chat_id= update.effective_chat.id
    query = update.callback_query
    df = get_on_sale()
    df = df.drop(int(query.data), axis = 0)
    df.to_csv('data/on_sale.csv')
    query.edit_message_text(text=f"Eliminazione del libro selezionato...")
    context.bot.send_message(chat_id, "Libro eliminato.")
