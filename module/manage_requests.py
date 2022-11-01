from winreg import QueryInfoKey
import yaml
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.create_connection import connect_and_execute, create_connection
from module.add_item import add_item
from module.find import find
from module.send_results import get_item_info
from module.shared import *


def get_group_id() -> int:
    with open(YAML_PATH, 'r') as yaml_config:
            config_map = yaml.load(yaml_config, Loader = yaml.SafeLoader)
    return int(config_map['admin_group_id'])


def add_request(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str, username: str, price: str) -> int:
    item = (str(chat_id), isbn, title, authors, username, price)
    query = "INSERT INTO Requests(ChatID, ISBN, Title, Authors, Seller, Price) VALUES(?,?,?,?,?,?)" 
    return connect_and_execute(context, chat_id, query, item, INSERT)


def delete_request(context: CallbackContext, row_id: int) -> None:
    query = "DELETE FROM Requests WHERE rowid=?"
    connect_and_execute(context, get_group_id(), query, (row_id,), DELETE)


def send_request(context: CallbackContext, row_id: int) -> None:
    group_id = get_group_id()
    
    keyboard = [[InlineKeyboardButton(YES, callback_data = (NEW_REQUEST_APPROVED + str(row_id)))], [InlineKeyboardButton(NO, callback_data = (NEW_REQUEST_DECLINED + str(row_id)))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query = "SELECT ISBN, Title, Authors, Seller, Price FROM Requests WHERE rowid=?"
    rows = connect_and_execute(context, group_id, query, (row_id,), SELECT) #maybe (row_id,)
    
    isbn, title, authors, username, price = rows[0]
    context.bot.send_message(group_id, PENDING_REQUEST + get_item_info(isbn, title, authors, username, price), reply_markup = reply_markup)


def update_similar_requests(context: CallbackContext, isbn: str) -> None:
    group_id = get_group_id()
    
    query = "SELECT rowid, ChatID, Seller, Price FROM Requests WHERE ISBN=?"
    rows = connect_and_execute(context, group_id, query, (isbn,), SELECT)   # maybe (isbn,)

    book_info = find(context, group_id, isbn, BOOKS)
    _, title, authors = book_info[0]
    
    for i in range(len(rows)):
        row_id, chat_id, username, price = rows[i]
        add_item(context, chat_id, isbn, title, authors, username, price)
        delete_request(row_id)
        context.bot.send_message(chat_id, ON_SALE_CONFIRM)
