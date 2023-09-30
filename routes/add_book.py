from flask import Response, request
from routes.validate import validate
from routes.utils import respond
from routes._data import _find, _add_book, _add_item
from module.shared import PRICE_ERROR, USERNAME_ERROR, ISBN_ERROR, ON_SALE_CONFIRM, BOOK_NOT_AVAILABLE, BOOKS
from module.utils import check_isbn, check_price, data_from_soup
from module.book_in_unict import book_in_unict


def sell() -> Response:
    """
    Adds a book into the market. 
    Required parameters in JSON body:
    :init_data: — the query string passed by telegram
    :web_app: — whether data is coming from webapp (False for login widget)
    :isbn: — ISBN code of the book
    :price: — Insertion price (float, string, dot or comma separated)
    """

    # Validating telegram data
    user = validate()
    if type(user) == Response:
        # Telegram data is invalid.
        return user
    
    # Checking username
    username = user.get('username', None)
    if not username:
        return respond({'message': USERNAME_ERROR}, success = False)
    username = '@' + username
    # Checking ISBN
    user_isbn = request.json.get('isbn', 'None')
    if not check_isbn(user_isbn):
        return respond({'message': ISBN_ERROR}, success = False)
    # Checking price
    # price = format(float(request.json.get('price', '-1.0').replace(',', '.')), '.2f')
    price = request.json.get('price', None)
    if not check_price(price):
        return respond({'message': PRICE_ERROR}, success = False)
    
    # Searching ISBN in local database
    search = _find(user['id'], user_isbn)
    if search['success'] and search['result']:
        # Found in local database.
        isbn, title, authors = search['result'][0]
    else:
        # Not found. Searching ISBN in unict
        found, soup = book_in_unict(user_isbn)
        if found:
            # Found in unict.
            isbn, title, authors = data_from_soup(soup)
            # Adding book to the local database in case it's missing
            if not _find(user['id'], isbn):
                result = _add_book(user['id'], isbn, title, authors)
                if not result['success']: pass # not critical, ignoring
        else:
            # Book not found in both local and unict.
            return respond({'message': BOOK_NOT_AVAILABLE}, success = False)
    
    # All fine. Adding to the insertions database and returning
    result = _add_item(user['id'], isbn, title, authors, username, price)
    return respond({
        'message': ON_SALE_CONFIRM if result['success'] else result['resultz'],
        'title': title,
        'authors': authors
    }, success = result['success'])
