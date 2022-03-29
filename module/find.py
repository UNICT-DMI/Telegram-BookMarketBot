import sqlite3

def find(txt: str, conn:sqlite3.Connection, s:str):
    cur = conn.cursor()
    if s == 'Books':
        cur.execute("SELECT * FROM Books WHERE ISBN=?", (txt,))
    else:
        q = '%'+txt+'%'
        cur.execute("SELECT rowid, * FROM Market WHERE Titolo LIKE ? OR ISBN Like ? OR Autori LIKE ?", (q, q, q,))
    rows = cur.fetchall()
    return rows
