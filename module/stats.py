"""/stats command"""
from telegram import Update
from telegram.ext import CallbackContext
from module.shared import SELECT, STATS_MESSAGE, DB_ERROR
from module.create_connection import connect_and_execute


def stats(update: Update, context: CallbackContext) -> None:
    """called by /stats
        It returns the number of books that are now on sale

        Args:
            update: update event
            context: context passed by the handler"""

    query = "SELECT COUNT(*) FROM Market"
    chat_id = update.effective_chat.id

    try:
        num: int = connect_and_execute(
            context=context, chat_id=chat_id, query=query, params=(), operation=SELECT
        )[0][0]
        context.bot.send_message(chat_id=chat_id, text=STATS_MESSAGE+str(num))
    except ValueError as v:
        print(str(v))
        context.bot.send_message(chat_id=chat_id, text=DB_ERROR)
