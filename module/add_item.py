from module.create_connection import create_connection
from module.shared import DB_PATH


def add_item(isbn: str, title: str, authors: str, username: str, price: str) -> None:
    item = (isbn, title, authors, username, price)
    sql = """ INSERT INTO Market(ISBN, Titolo, Autori, Venditore, Prezzo)
              VALUES(?,?,?,?,?) """
    conn = create_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
    conn.close()
