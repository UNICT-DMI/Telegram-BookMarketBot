from telegram import Update
from telegram.ext import CallbackContext
from module.add_book import add_book
from module.add_item import add_item
from module.create_connection import create_connection
from module.shared import *
from module.add_book import add_book
from module.add_item import add_item
from module.manage_requests import delete_request, update_similar_requests


def button(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query
    operation = query.data.split(';')[0]

    if operation == DELETE:
        conn = create_connection(DB_PATH)
        if conn:
            cur = conn.cursor()
            _, q = query.data.split(';')
            cur.execute("DELETE FROM Market WHERE rowid=?", (q,))
            query.edit_message_text(text = DELETING)
            conn.commit()
            context.bot.send_message(chat_id, DELETED)
        else:
            query.edit_message_text(text = DB_ERROR)
        conn.close()
    
    if operation == NEW_REQUEST:
        _, vote, row_id = query.data.split(';')
        
        conn = create_connection(DB_PATH)
        if not conn:
            context.bot.send_message(chat_id, DB_ERROR)
            return
        cur = conn.cursor()
        cur.execute("SELECT rowid, * FROM Requests WHERE rowid=?", (row_id,))
        rows = cur.fetchall()
        
        if rows:

            if vote == YES:
                _, chat_id, isbn, title, authors, username, price = rows[0]
                query.edit_message_text(text = ADMIN_REQUEST_ACCEPTED)
                add_book(isbn, title, authors)
                add_item(isbn, title, authors, username, price)
                delete_request(context, chat_id, row_id)
                update_similar_requests(context, isbn)
                context.bot.send_message(chat_id, USER_REQUEST_ACCEPTED)
            
            if vote == NO:
                chat_id = rows[0][1]
                query.edit_message_text(text = ADMIN_REQUEST_DECLINED)
                delete_request(context, chat_id, row_id)
                context.bot.send_message(chat_id, USER_REQUEST_DECLINED)
        
        else:
            if vote == YES or vote == NO:
                query.edit_message_text(text = CASCADE_REQUEST)

        conn.close()
