import sqlite3

def add_book(conn: sqlite3.Connection, isbn: str, title: str, authors:str) -> None:
    book = (isbn, title, authors)
    sql = ''' INSERT INTO Books(ISBN, Titolo, Autori)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
