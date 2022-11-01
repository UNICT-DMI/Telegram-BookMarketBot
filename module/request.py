import bs4
from telegram import Update
from telegram.ext import CallbackContext
from module.add_item import add_item
from module.add_book import add_book
from module.find import find
from module.book_in_unict import book_in_unict
from module.create_connection import connect_and_execute
from module.manage_requests import add_request, send_request
from module.send_results import get_book_info
from module.shared import PRICE_ERROR,USERNAME_ERROR,ISBN_ERROR,REQUEST_USAGE,REQUEST_SENT,REQUEST_ALREADY_SENT,BOOK_IS_PRESENT,ON_SALE_CONFIRM,BOOKS,SELECT


def _get_isbn_from_website(soup: bs4.BeautifulSoup) -> str:
    idx = len(str(soup.findAll("td")).split("bibInfoData")) - 1
    return str(soup.findAll("td")) \
        .split("bibInfoData")[idx] \
        .split("\n")[1] \
        .split("<")[0]


def request(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message == "/richiedi" or len(message.split('; ')) != 4:
        context.bot.send_message(chat_id, REQUEST_USAGE)
        return

    username = "@" + str(context.bot.get_chat(chat_id)["username"])
    if username.lower() == "@none":
        context.bot.send_message(chat_id, USERNAME_ERROR)
        return

    user_isbn = message.split('; ')[0].split()[1]
    if len(user_isbn) != 10 and len(user_isbn) != 13:
        context.bot.send_message(chat_id, ISBN_ERROR)
        return

    try:
        format(float(message.split('; ')[1].replace(",", ".")), ".2f")
        price = str(format(float(message.split('; ')[1].replace(",", ".")), ".2f"))

        rows = find(context, chat_id, user_isbn, BOOKS)

        if rows:
            isbn, title, authors = rows[0]
            context.bot.send_message(chat_id, BOOK_IS_PRESENT + get_book_info(isbn, title, authors))
            add_item(context, chat_id, isbn, title, authors, username, price)
            context.bot.send_message(chat_id, ON_SALE_CONFIRM)
            return

        found, soup = book_in_unict(user_isbn)
        if found:
            isbn = _get_isbn_from_website(soup)
            title, authors = soup.find("strong").text.split("/")
            context.bot.send_message(chat_id, BOOK_IS_PRESENT + get_book_info(isbn, title, authors))
            add_book(context, chat_id, isbn, title, authors)
            add_item(context, chat_id, isbn, title, authors, username, price)
            context.bot.send_message(chat_id, ON_SALE_CONFIRM)
            return

        _, _, title, authors = message.split('; ')

        query = "SELECT * FROM Requests WHERE ISBN=? AND Seller=?"
        params = (user_isbn, username,)

        rows = connect_and_execute(context, chat_id, query, params, SELECT)
        if not rows:
            row_id = add_request(context, chat_id, user_isbn, title, authors, username, price)
            send_request(context, row_id)
            message_text = REQUEST_SENT
        else:
            message_text = REQUEST_ALREADY_SENT

        context.bot.send_message(chat_id, message_text)

    # pylint: disable=broad-except
    except Exception as e:
        print(str(e))
        context.bot.send_message(chat_id, PRICE_ERROR)
