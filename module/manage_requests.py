import yaml
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.add_item import add_item
from module.find import find
from module.send_results import get_item_info
from module.shared import *


def get_group_id() -> str:
    with open(YAML_PATH, 'r') as yaml_config:
            config_map = yaml.load(yaml_config, Loader = yaml.SafeLoader)
    return config_map['admin_group_id']


def add_request(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str, username: str, price: str) -> int:
    item = (chat_id, isbn, title, authors, username, price)
    sql = """ INSERT INTO Requests(ChatID, ISBN, Title, Authors, Seller, Price)
              VALUES(?,?,?,?,?,?) """
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, DB_ERROR)
        return
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
    conn.close()
    return cur.lastrowid

def delete_request(context: CallbackContext, chat_id: int, row_id: int) -> None:
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, DB_ERROR)
        return
    cur = conn.cursor()
    cur.execute("DELETE FROM Requests WHERE rowid=?", (row_id,))
    conn.commit()
    conn.close()

def send_request(context: CallbackContext, row_id: int) -> None:
    group_id = get_group_id()
    
    keyboard = [[InlineKeyboardButton(YES, callback_data = (NEW_REQUEST_APPROVED + str(row_id)))], [InlineKeyboardButton(NO, callback_data = (NEW_REQUEST_DECLINED + str(row_id)))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(group_id, DB_ERROR)
        return
    cur = conn.cursor()
    cur.execute("SELECT ISBN, Title, Authors, Seller, Price FROM Requests WHERE rowid=?", (row_id,))
    rows = cur.fetchall()
    conn.close()
    
    isbn, title, authors, username, price = rows[0]
    context.bot.send_message(group_id, PENDING_REQUEST + get_item_info(isbn, title, authors, username, price), reply_markup = reply_markup)

def update_similar_requests(context: CallbackContext, isbn: str) -> None:
    group_id = get_group_id()
    
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(group_id, DB_ERROR)
        return
    cur = conn.cursor()
    cur.execute("SELECT rowid, ChatID, Seller, Price FROM Requests WHERE ISBN=?", (isbn,))
    rows = cur.fetchall()
    
    book_info = find(isbn, conn, BOOKS)
    _, title, authors = book_info[0]
    
    for i in range(len(rows)):
        row_id, chat_id, username, price = rows[i]
        add_item(isbn, title, authors, username, price)
        delete_request(row_id)
        context.bot.send_message(chat_id, ON_SALE_CONFIRM)
    
    conn.close()
