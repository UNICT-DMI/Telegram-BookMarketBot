import bs4
import re
from telegram import Update
from telegram.ext import CallbackContext
from module.add_item import add_item
from module.add_book import add_book
from module.find import find
from module.book_in_unict import book_in_unict
from module.send_results import get_book_info
from module.shared import PRICE_ERROR,USERNAME_ERROR,ISBN_ERROR,SELL_USAGE,ISBN_PREFIX_1,ISBN_PREFIX_2,ON_SALE_CONFIRM,BOOKS,SEARCHING_ISBN,BOOK_NOT_AVAILABLE


def _get_isbn_from_website(soup: bs4.BeautifulSoup) -> str:
    idx = len(str(soup.findAll("td")).split("bibInfoData")) - 1
    isbn = str(soup.findAll("td")) \
        .split("bibInfoData")[idx] \
        .split("\n")[1] \
        .split("<")[0]
    isbn = isbn.replace('-','')
    if len(isbn) > 13:
        p1 = re.search(ISBN_PREFIX_1, isbn)
        if p1 is not None:
            s = p1.span()[0]
            return isbn[s:s+13]

        p2 = re.search(ISBN_PREFIX_2, isbn)
        if p2 is not None:
            s = p2.span()[0]
            return isbn[s:s+13]
    return isbn


def sell(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message == "/vendi":
        context.bot.send_message(chat_id, SELL_USAGE)
        return

    username = "@" + str(context.bot.get_chat(chat_id)["username"])
    if username.lower() == "@none":
        context.bot.send_message(chat_id, USERNAME_ERROR)
        return

    user_isbn = message.split()[1]
    if len(user_isbn) != 10 and len(user_isbn) != 13:
        context.bot.send_message(chat_id, ISBN_ERROR)
        return

    try:
        format(float(message.split()[2].replace(",", ".")), ".2f")
        price = str(format(float(message.split()[2].replace(",", ".")), ".2f"))
        context.bot.send_message(chat_id, SEARCHING_ISBN)

        rows = find(context, chat_id, user_isbn, BOOKS)

        if rows:
            isbn, title, authors = rows[0]
            context.bot.send_message(chat_id, get_book_info(isbn, title, authors))
            add_item(context, chat_id, isbn, title, authors, username, price)
            context.bot.send_message(chat_id, ON_SALE_CONFIRM)
            return

        found, soup = book_in_unict(user_isbn)
        if found:
            isbn = _get_isbn_from_website(soup)
            title, authors = soup.find("strong").text.split("/")
            context.bot.send_message(chat_id, get_book_info(isbn, title, authors))
            if not find(context, chat_id, isbn, BOOKS):
                add_book(context, chat_id, isbn, title, authors)
            add_item(context, chat_id, isbn, title, authors, username, price)
            context.bot.send_message(chat_id, ON_SALE_CONFIRM)
            return

        context.bot.send_message(chat_id, BOOK_NOT_AVAILABLE)

    # pylint: disable=broad-except
    except Exception as e:
        print(str(e))
        context.bot.send_message(chat_id, PRICE_ERROR)
