from typing import List
from telegram.ext import CallbackContext


def send_results(rows: List, chat_id: int, context: CallbackContext) -> None:
    res = ""
    for i in range(len(rows)):
        res += ("n°: " + str(i + 1) + "\n" + get_item_info(rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5]) + "\n")
        if (i + 1) % 3 == 0:
            context.bot.send_message(chat_id, res)
            res = ""
    if res != "":
        context.bot.send_message(chat_id, res)

def get_book_info(isbn: str, title: str, authors: str) -> str:
    s = "ISBN: " + isbn + "\n" + "Titolo: " + title + "\n" + "Autori: " + authors + "\n"
    return s

def get_item_info(isbn: str, title: str, authors: str, seller: str, price: str) -> str:
    s = "ISBN: " + isbn + "\n" + "Titolo: " + title + "\n" + "Autori: " + authors + "\n" + "Venditore: " + seller + "\n" + "Prezzo: " + price + " €\n"
    return s
