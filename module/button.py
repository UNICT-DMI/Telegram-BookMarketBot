from telegram import Update
from telegram.ext import CallbackContext
from module.add_book import add_book
from module.add_item import add_item
from module.create_connection import connect_and_execute
from module.shared import *
from module.manage_requests import delete_request, update_similar_requests


def button(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query
    operation = query.data.split(';')[0]

    if operation == DELETE:
        sql = "DELETE FROM Market WHERE rowid=?"
        _, q = query.data.split(';')
        connect_and_execute(context, chat_id, sql, (int(q),), DELETE)
        query.edit_message_text(text = DELETING)
        context.bot.send_message(chat_id, DELETED)
    
    if operation == NEW_REQUEST:
        _, vote, row_id = query.data.split(';')
        sql = "SELECT rowid, * FROM Requests WHERE rowid=?"
        rows = connect_and_execute(context, chat_id, sql, (int(row_id),), SELECT)
        
        if rows:

            if vote == YES:
                _, chat_id, isbn, title, authors, username, price = rows[0]
                query.edit_message_text(text = ADMIN_REQUEST_ACCEPTED)
                add_book(context, chat_id, isbn, title, authors)
                add_item(context, chat_id, isbn, title, authors, username, price)
                delete_request(context, int(row_id))
                update_similar_requests(context, isbn)
                context.bot.send_message(chat_id, USER_REQUEST_ACCEPTED)
            
            if vote == NO:
                chat_id = rows[0][1]
                query.edit_message_text(text = ADMIN_REQUEST_DECLINED)
                delete_request(context, int(row_id))
                context.bot.send_message(chat_id, USER_REQUEST_DECLINED)
        
        else:
            if vote == YES or vote == NO:
                query.edit_message_text(text = CASCADE_REQUEST)
