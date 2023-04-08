from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.my_books import get_user_books
from module.shared import DELETE_USAGE, DELETE_APPROVED, SELECT_BOOK_TO_DELETE


def delete(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message != "/elimina":
        context.bot.send_message(chat_id, DELETE_USAGE)
        return

    rows = get_user_books(context, chat_id)
    if rows:
        keyboard = [
            [
                InlineKeyboardButton(
                    str(i + 1),
                    callback_data=DELETE_APPROVED + str(rows[i][0])
                )
            ] for i in range(len(rows))
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(SELECT_BOOK_TO_DELETE, reply_markup = reply_markup)
