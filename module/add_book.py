from module.create_connection import connect_and_execute
from module.shared import INSERT
from telegram.ext import CallbackContext

def add_book(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str) -> None:
    query = "INSERT INTO Books(ISBN, Title, Authors) VALUES(?,?,?)"
    params = (isbn, title, authors)
    connect_and_execute(context, chat_id, query, params, INSERT)
