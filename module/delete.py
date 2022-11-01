from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.my_books import get_user_books


def delete(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message != "/elimina":
        context.bot.send_message(chat_id, "Utilizzo comando: /elimina")
        return

    rows = get_user_books(context, chat_id)
    if rows:
        keyboard = [[InlineKeyboardButton(str(i + 1), callback_data=(rows[i][0]))] for i in range(len(rows))]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Quale libro vuoi eliminare?", reply_markup=reply_markup)
