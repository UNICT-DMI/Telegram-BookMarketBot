from module.create_connection import connect_and_execute
from module.shared import INSERT
from telegram.ext import CallbackContext

# pylint: disable=too-many-arguments
def add_item(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str, username: str, price: str) -> None:
    query = "INSERT INTO Market(ISBN, Title, Authors, Seller, Price) VALUES(?,?,?,?,?)"
    params = (isbn, title, authors, username, price)
    connect_and_execute(context, chat_id, query, params, INSERT)
