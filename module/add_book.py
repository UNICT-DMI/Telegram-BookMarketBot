from module.create_connection import create_connection
from module.shared import DB_PATH


def add_book(isbn: str, title: str, authors: str) -> None:
    book = (isbn, title, authors)
    sql = """ INSERT INTO Books(ISBN, Title, Authors)
              VALUES(?,?,?) """
    conn = create_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    conn.close()
