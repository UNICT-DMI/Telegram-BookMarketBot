from module.shared import USERNAME_ERROR
from routes._data import _get_user_books
from routes.validate import validate
from routes.utils import respond
from flask import Response

def mybooks() -> Response:
    """
    Adds a book into the market. 
    Required parameters in JSON body:
    :init_data: — the query string passed by telegram
    :web_app: — whether data is coming from webapp (False for login widget)
    """

    # Validating telegram data
    user = validate()
    if type(user) == Response:
        # Telegram data is invalid.
        return user
    else:
        # Checking username
        username = user.get('username', None)
        if not username:
            return respond({'message': USERNAME_ERROR}, success = False)
        else: username = '@' + username

        query = _get_user_books(user['id'], username)
        return respond(query, success = query['success'])