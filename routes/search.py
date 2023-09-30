from flask import request
from module.create_connection import create_connection
from module.shared import DB_PATH, DB_ERROR
from module.find import app_find
from routes.utils import respond


# search books in the
# bot's local database
def search():
    # getting user input
    query = request.args.get('q')

    # creating connection
    conn = create_connection(DB_PATH)
    if not conn:
        # returning error message
        return respond({'message': DB_ERROR}, success = False)

    # querying the database
    rows = app_find(query, conn, "Market")
    # closing connection
    conn.close()
    # returning results
    return respond({'results': rows})