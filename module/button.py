from telegram import Update
from telegram.ext import CallbackContext
from module.add_book import add_book
from module.add_item import add_item
from module.create_connection import create_connection
from module.shared import DB_PATH, error_message
from module.add_book import add_book
from module.add_item import add_item
from module.manage_requests import delete_request, update_similar_requests


def button(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    query = update.callback_query
    
    if query.data.split(';')[0] == 'delete':
        conn = create_connection(DB_PATH)
        if conn:
            cur = conn.cursor()
            q = query.data.split(';')[1]
            cur.execute("DELETE FROM Market WHERE rowid=?", (q,))
            query.edit_message_text(text=f"Eliminazione del libro selezionato...")
            conn.commit()
            context.bot.send_message(chat_id, "Libro eliminato.")
        else:
            query.edit_message_text(text=f"Si è verificato un problema nella lettura del database.")
        conn.close()
    
    if query.data.split(';')[0] == 'new_request':
        vote = query.data.split(';')[1]
        row_id = query.data.split(';')[2]
        
        conn = create_connection(DB_PATH)
        if not conn:
            context.bot.send_message(chat_id, error_message)
            return
        cur = conn.cursor()
        cur.execute("SELECT rowid, * FROM Requests WHERE rowid=?", (row_id,))
        rows = cur.fetchall()
        
        if rows:

            if vote == 'Y':
                _, chat_id, isbn, title, authors, username, price = rows[0]
                query.edit_message_text(text=f"Richiesta accettata.")
                add_book(isbn, title, authors)
                add_item(isbn, title, authors, username, price)
                delete_request(context, chat_id, row_id)
                update_similar_requests(context, isbn)
                context.bot.send_message(chat_id, "Il libro è stato messo in vendita.")
            
            if vote == 'N':
                chat_id = rows[0][1]
                query.edit_message_text(text=f"Richiesta rifiutata.")
                delete_request(context, chat_id, row_id)
                context.bot.send_message(chat_id, "La tua richiesta è stata rifiutata. Controlla se i dati inseriti sono corretti e riprova.")
        
        else:
            if vote == 'Y' or vote == 'N':
                query.edit_message_text(text=f"Richiesta accettata a cascata precedentemente.")

        conn.close()
