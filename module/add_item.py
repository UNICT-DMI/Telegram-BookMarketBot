import sqlite3

def add_item(conn: sqlite3.Connection, isbn: str, title: str, authors:str, username:str, price:str) -> None:
    item = (isbn, title, authors, username, price)
    sql = ''' INSERT INTO Market(ISBN, Titolo, Autori, Venditore, Prezzo)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
