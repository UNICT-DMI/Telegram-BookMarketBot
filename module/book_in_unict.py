from typing import Tuple
from bs4 import BeautifulSoup
import requests


def book_in_unict(user_isbn: str) -> Tuple:
    url = ("https://catalogo.unict.it/search/i?SEARCH=" + user_isbn + "&sortdropdown=-&searchscope=9")
    x = requests.get(url, timeout=10)
    soup = BeautifulSoup(x.content, "html.parser")
    check = str(soup.findAll("td"))
    if "No matches found" not in check:
        return (True, soup)
    return (False, None)
