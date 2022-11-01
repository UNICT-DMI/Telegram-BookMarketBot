from bs4 import BeautifulSoup
import requests
from module.shared import URL_1, URL_2, NO_MATCHES

def book_in_unict(user_isbn: str) -> tuple:
    url = (URL_1 + user_isbn + URL_2)
    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")
    check = str(soup.findAll("td"))
    if NO_MATCHES not in check:
        return (True, soup)
    return (False, None)
