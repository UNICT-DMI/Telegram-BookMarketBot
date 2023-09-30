from flask import request, Response
from module.shared import USERNAME_ERROR, MISSING_FIELD, DELETE_UNAUTHORIZED
from routes._data import _get_item, _remove_item
from routes.validate import validate
from routes.utils import respond

def delete() -> Response:
    """
    Deletes a book from the market. 
    Required parameters in JSON body:
    :init_data: — the query string passed by telegram
    :web_app: — whether data is coming from webapp (False for login widget)
    :insertion_id: — row_id of the insertion to remove
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
        # Getting insertion id
        insertion_id = request.json.get('insertion_id', None)
        if insertion_id is None:
            return respond({'message': MISSING_FIELD('insertion_id')}, success = False)
        # Ensure insertion was published by the same person
        insertion = _get_item(insertion_id)
        if insertion['success']:
            if insertion['result'][0][3] == username:
                # Performing operation and returning
                query = _remove_item(insertion_id)
                return respond(query, success = query['success'])
            else:
                return respond({'message': DELETE_UNAUTHORIZED}, success = False)
        else: return respond(insertion, success = False)