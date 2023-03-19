from module.create_connection import connect_and_execute
from module.shared import INSERT
from telegram.ext import CallbackContext

def add_book(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str) -> None:
    """called in the request of a book or in selling books
        Add a book in the Books table

        Args:
            context: context passed by the handler
            chat_id: id of the chat of the message
            isbn: isbn of the book to add
            title: title of the book to add
            authors: authors of the book to add
    """
    query = "INSERT INTO Books(ISBN, Title, Authors) VALUES(?,?,?)"
    params = (isbn, title, authors)
    connect_and_execute(context, chat_id, query, params, INSERT)
