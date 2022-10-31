from typing import List
import sqlite3
from module.shared import BOOKS


def find(txt: str, conn: sqlite3.Connection, s: str) -> List[tuple]:
    cur = conn.cursor()
    if s == BOOKS:
        cur.execute("SELECT * FROM Books WHERE ISBN=?", (txt,))
    else:
        q = "%" + txt + "%"
        cur.execute("SELECT rowid, * FROM Market WHERE Title LIKE ? OR ISBN Like ? OR Authors LIKE ?", (q, q, q,))
    rows = cur.fetchall()
    return rows
