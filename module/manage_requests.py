import yaml
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from module.create_connection import create_connection
from module.add_item import add_item
from module.find import find
from module.shared import DB_PATH, error_message


def add_request(context: CallbackContext, chat_id: int, isbn: str, title: str, authors: str, username: str, price: str) -> None:
    item = (chat_id, isbn, title, authors, username, price)
    sql = """ INSERT INTO Requests(ChatID, ISBN, Title, Authors, Seller, Price)
              VALUES(?,?,?,?,?,?) """
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, error_message)
        return
    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()
    conn.close()
    return cur.lastrowid

def delete_request(context: CallbackContext, chat_id: int, row_id: int) -> None:
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(chat_id, error_message)
        return
    cur = conn.cursor()
    cur.execute("DELETE FROM Requests WHERE rowid=?", (row_id,))
    conn.commit()
    conn.close()

def send_request(context: CallbackContext, row_id: int) -> None:
    with open('config/settings.yaml', 'r') as yaml_config:
            config_map = yaml.load(yaml_config, Loader=yaml.SafeLoader)
    group_id = config_map['admin_group_id']
    keyboard = [[InlineKeyboardButton('Y', callback_data=('new_request;Y;' + str(row_id)))], [InlineKeyboardButton('N', callback_data=('new_request;N;'+ str(row_id)))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(group_id, error_message)
        return
    cur = conn.cursor()
    cur.execute("SELECT ISBN, Title, Authors, Seller, Price FROM Requests WHERE rowid=?", (row_id,))
    rows = cur.fetchall()
    conn.close()
    
    isbn = rows[0][0]
    title = rows[0][1]
    authors = rows[0][2]
    username = rows[0][3]
    price = rows[0][4]
    context.bot.send_message(group_id, "New Pending Request:\n"+isbn+"\n"+title+"\n"+authors+"\n"+username+"\n"+price+"\n", reply_markup=reply_markup)

def update_similar_requests(context: CallbackContext, isbn: str) -> None:
    with open('config/settings.yaml', 'r') as yaml_config:
            config_map = yaml.load(yaml_config, Loader=yaml.SafeLoader)
    group_id = config_map['admin_group_id']
    
    conn = create_connection(DB_PATH)
    if not conn:
        context.bot.send_message(group_id, error_message)
        return
    cur = conn.cursor()
    cur.execute("SELECT rowid, ChatID, Seller, Price FROM Requests WHERE ISBN=?", (isbn,))
    rows = cur.fetchall()
    
    book_info = find(isbn, conn, 'Books')
    title = book_info[0][1]
    authors = book_info[0][2]
    
    for i in range(len(rows)):
        row_id = rows[i][0]
        chat_id = rows[i][1]
        username = rows[i][2]
        price = rows[i][3]
    
        add_item(isbn, title, authors, username, price)
        delete_request(row_id)
        context.bot.send_message(chat_id, "Il libro è stato messo in vendita.")
    
    conn.close()

    
    
    
