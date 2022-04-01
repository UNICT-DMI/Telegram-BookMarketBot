import sqlite3
from sqlite3 import Error


def create_connection(db_file: str) -> sqlite3.Connection:
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(str(e))
    return conn
