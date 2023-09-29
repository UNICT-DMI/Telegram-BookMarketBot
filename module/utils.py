from module.sell import _get_isbn_from_website
from module.shared import URL_1, URL_2, NO_MATCHES
from telegram.ext import CallbackContext
from bs4 import BeautifulSoup
from typing import Callable
import requests


def check_isbn(isbn: str) -> bool:
    "Checks whether an ISBN code is valid."
    # Example: "9788838667510"
    if len(isbn) == 10:
        # 1. Multiply each number by its position number and then sum up the products.
        val = sum([int(isbn[i-1]) * len(isbn) - i + 1 for i in range(1, len(isbn) + 1)])
        # 2. Divide the sum by 11 and find out what is the remainder. 
        # If the remainder is zero, then it is a valid 10 digit ISBN.
        # If the remainder is not zero, then it is not a valid 10 digit ISBN.
        return val % 11 == 0
    elif len(isbn) == 13:
        # 1. Multiply each number by an alternating 1 and 3 and then sum up the products.
        # Odd number positions by 1.
        # Even number positions by 3.
        val = sum([int(isbn[i-1]) * (3 if i % 2 == 0 else 1) for i in range(1, len(isbn) + 1)])
        # Divide the sum by 10 and find out what is the remainder.
        # If the remainder is zero, then it is a valid 13 digit ISBN.
        # If the remainder is not zero, then it is not a valid 13 digit ISBN.
        return val % 10 == 0
    return False


def check_price(price: str) -> str:
    "Returns the price in .2f form, if valid."
    price = str(price).replace(',', '.')
    if price.replace(".", "", 1).isdigit():
        return format(float(price), '.2f')
    else: return False


def data_from_soup(soup: BeautifulSoup) -> (str, str, str):
    isbn = _get_isbn_from_website(soup)
    title, authors = soup.find("strong").text.split("/")
    return isbn, title, authors
