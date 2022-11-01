from typing import Union
import sqlite3
from telegram.ext import CallbackContext
from module.create_connection import connect_and_execute
from module.shared import BOOKS, SELECT


def find(context: CallbackContext, chat_id: int, txt: str, mode: str) -> Union[int, list, None]:
    if mode == BOOKS:
        query = "SELECT * FROM Books WHERE ISBN=?"
        params = (txt,)
    else:
        q = "%" + txt + "%"
        query = "SELECT rowid, * FROM Market WHERE Title LIKE ? OR ISBN Like ? OR Authors LIKE ?"
        params = (q, q, q,)

    return connect_and_execute(context, chat_id, query, params, SELECT)


def app_find(txt: str, conn: sqlite3.Connection, s: str) -> list[tuple]:
    cur = conn.cursor()
    if s == "Books":
        cur.execute("SELECT * FROM Books WHERE ISBN=?", (txt,))
    else:
        q = "%" + txt + "%"
        cur.execute("SELECT rowid, * FROM Market WHERE Title LIKE ? OR ISBN Like ? OR Authors LIKE ?", (q, q, q,))
    rows = cur.fetchall()
    return rows
