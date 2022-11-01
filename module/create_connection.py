import sqlite3
from sqlite3 import Error
from module.shared import DB_PATH, DB_ERROR, INSERT, DELETE, SELECT
from telegram.ext import CallbackContext
from typing import Optional, Union

def create_connection(db_file: str) -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(str(e))
    return conn


# pylint: disable=inconsistent-return-statements
def connect_and_execute(context: CallbackContext, chat_id: int, query: str, params: tuple, operation: str) -> Optional[Unionint, list]]:
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, DB_ERROR)
        return

    cur = conn.cursor()
    cur.execute(query, params)
    if operation == INSERT:
        conn.commit()
        last_row_id = cur.lastrowid
        conn.close()
        return last_row_id

    if operation == DELETE:
        conn.commit()
        conn.close()
        return

    if operation == SELECT:
        rows = cur.fetchall()
        conn.close()
        return rows
        