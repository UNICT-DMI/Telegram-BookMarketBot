import pandas as pd
from module.get_books import get_books
from module.shared import BOOKS_DB_PATH

def add_book(isbn: str, title: str, authors:str) -> None:
    books = get_books()
    new_book = pd.DataFrame({'ISBN':str(isbn),'Titolo':str(title), 'Autori':str(authors)}, index=[len(books)])
    books = pd.concat([books, new_book])
    books.to_csv(BOOKS_DB_PATH)
    