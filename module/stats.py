"""/stats command"""
from telegram import Update
from telegram.ext import CallbackContext
from module.shared import SELECT, STATS_MESSAGE
from module.create_connection import connect_and_execute

def stats(update: Update, context: CallbackContext) -> None:
    """called by /stats
        It returns the number of books that are now on sale

        Args:
            update: update event
            context: context passed by the handler"""

    query: str = "SELECT COUNT(*) FROM Market"
    chat_id: int = update.effective_chat.id
    params = ()
    num: int = connect_and_execute(
        context=context, chat_id=chat_id, query=query, params=params, operation=SELECT
    )[0][0]

    context.bot.send_message(chat_id=chat_id, text=STATS_MESSAGE+str(num))
