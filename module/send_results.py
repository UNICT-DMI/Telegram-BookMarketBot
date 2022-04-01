from typing import List
from telegram.ext import CallbackContext


def send_results(rows: List, chat_id: int, context: CallbackContext) -> None:
    res = ""
    for i in range(len(rows)):
        res += ("n°: " + str(i + 1) + "\n" + "ISBN: " + rows[i][1] + "\n" + "Titolo: " + rows[i][2] + "\n" + "Autori: " + rows[i][3] + "\n" + "Venditore: " + rows[i][4] + "\n" + "Prezzo: " + rows[i][5] + " €\n\n")
        if (i + 1) % 3 == 0:
            context.bot.send_message(chat_id, res)
            res = ""
    if res != "":
        context.bot.send_message(chat_id, res)
