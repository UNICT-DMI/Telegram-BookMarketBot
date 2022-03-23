from module.get_on_sale import get_on_sale
from telegram import Update
from telegram.ext import CallbackContext

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    df = get_on_sale()
    df = df.drop(int(query.data), axis = 0)
    df.to_csv('data.csv')
    query.edit_message_text(text=f"Libro eliminato.")