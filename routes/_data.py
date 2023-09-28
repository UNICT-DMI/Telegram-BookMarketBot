from module.create_connection import create_connection
from module.shared import DB_PATH, DB_ERROR, INSERT, DELETE, DELETED, SELECT

def _find(chat_id: str, isbn: str) -> dict:
    # Equivalent of module.find(..., 'Books'), but without
    # telegram.ext.CallbackContext as a parameter.
    query = "SELECT * FROM Books WHERE ISBN=?"
    params = (isbn, )
    return _connect_and_execute(query, params, SELECT)

# pylint: disable=too-many-arguments
def _add_item(chat_id: int, isbn: str, title: str, authors: str, username: str, price: str) -> dict:
    # Equivalent of module.add_item, but without
    # telegram.ext.CallbackContext as a parameter.
    query = "INSERT INTO Market(ISBN, Title, Authors, Seller, Price) VALUES(?,?,?,?,?)"
    params = (isbn, title, authors, username, price)
    return _connect_and_execute(query, params, INSERT)

def _get_item(row_id: int):
    sql = "SELECT * FROM Market WHERE rowid=?"
    return _connect_and_execute(sql, (int(row_id),), SELECT)

def _remove_item(row_id: int):
    sql = "DELETE FROM Market WHERE rowid=?"
    result = _connect_and_execute(sql, (int(row_id),), DELETE)
    if result['success']:
        return {'success': True, 'message': DELETED}
    else: return result

def _add_book(chat_id: int, isbn: str, title: str, authors: str) -> dict:
    # Equivalent of module.add_item, but without
    # telegram.ext.CallbackContext as a parameter.
    query = "INSERT INTO Books(ISBN, Title, Authors) VALUES(?,?,?)"
    params = (isbn, title, authors)
    return _connect_and_execute(query, params, INSERT)

# pylint: disable=inconsistent-return-statements
def _get_user_books(chat_id: int, username: str) -> dict:
    # Equivalent of module.get_user_books, but without
    # telegram.ext.CallbackContext as a parameter.
    conn = create_connection(DB_PATH)
    if not conn:
        return {'success': False, 'result': DB_ERROR}

    username = username if username.startswith("@") else "@" + username
    query = "SELECT rowid, * FROM Market WHERE Seller=?"
    rows = _connect_and_execute(query, (username,), SELECT)
    if rows['success']:
        return {'success': True, 'result': rows['result'] if rows['result'] else []}
    else:
        return {'success': False, 'message': rows['message']}


def _connect_and_execute(query: str, params: tuple, operation: str) -> dict:
    # Equivalent of module.create_connection.connect_and_execute,
    # but without telegram.ext.CallbackContext as a parameter.
    conn = create_connection(DB_PATH)
    if not conn:
        return {'success': False, 'result': DB_ERROR}

    cur = conn.cursor()
    cur.execute(query, params)

    if operation == INSERT:
        conn.commit()
        last_row_id = cur.lastrowid
        result = {'success': True, 'result': last_row_id}
    elif operation == DELETE:
        conn.commit()
        result = {'success': True, 'result': None}
    elif operation == SELECT:
        rows = cur.fetchall()
        result = {'success': True, 'result': rows}
    else:
        return {'success': False, 'result': 'Internal error: no OPERATION specified.'}
    
    conn.close()
    return result