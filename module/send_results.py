from typing import List
from telegram.ext import CallbackContext


def send_results(rows: List, chat_id: int, context: CallbackContext) -> None:
    res = ""
    # pylint: disable=consider-using-enumerate
    for i in range(len(rows)):
        res += ("n°: " + str(i + 1) + "\n" + get_item_info(rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5]) + "\n")
        if (i + 1) % 3 == 0:
            context.bot.send_message(chat_id, res)
            res = ""
    if res != "":
        context.bot.send_message(chat_id, res)


def get_book_info(isbn: str, title: str, authors: str) -> str:
    return f"Il libro è:\nISBN: {isbn} \nTitolo: {title}\nAutori: {authors}\n"


def get_item_info(isbn: str, title: str, authors: str, seller: str, price: str) -> str:
    return f"ISBN: {isbn} \nTitolo: {title}\nAutori: {authors}\nVenditore: {seller}\nPrezzo: {price} €\n"
    