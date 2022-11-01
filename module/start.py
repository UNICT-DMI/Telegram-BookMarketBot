from telegram import Update
from telegram.ext import CallbackContext
from module.shared import START_MESSAGE

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, START_MESSAGE)
