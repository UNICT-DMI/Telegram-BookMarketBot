from telegram import Update
from telegram.ext import CallbackContext
from module.add_item import add_item
from module.add_book import add_book
from module.find import find
from module.book_in_unict import book_in_unict
from module.create_connection import create_connection
from module.shared import DB_PATH

def sell(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message!="/vendi":
        username ="@"+str(context.bot.get_chat(chat_id)['username'])
        if username.lower() != '@none':
            user_isbn = message.split()[1]
            if len(user_isbn) == 10 or len(user_isbn) == 13:
                try:
                    format(float(message.split()[2].replace(',', '.')), '.2f')
                    price = str(format(float(message.split()[2].replace(',', '.')), '.2f'))
                    context.bot.send_message(chat_id, "Ricerca del libro associato all'ISBN inserito...")
                    
                    conn = create_connection(DB_PATH)
                    if conn:
                        rows = find(user_isbn, conn, 'Books')
                        if rows:
                            isbn = rows[0][0]
                            title  = rows[0][1]
                            authors  = rows[0][2]
                            title_and_authors  = title + "di" + authors
                            context.bot.send_message(chat_id, "Il libro è: \nTitolo: \"" + title_and_authors + "\"")
                            add_item(conn, isbn, title, authors, username, price)
                            context.bot.send_message(chat_id, "Il libro è stato aggiunto al database.")
                            return
                        
                        found, soup = book_in_unict(user_isbn)
                        if found:
                            isbn = str(soup.findAll('td')).split("bibInfoData")[len(str(soup.findAll('td')).split("bibInfoData"))-1].split("\n")[1].split("<")[0]
                            title  = soup.find('strong').text.split('/')[0]
                            authors  = soup.find('strong').text.split('/')[1]
                            title_and_authors  = soup.find('strong').text
                            context.bot.send_message(chat_id, "Il libro è: \nTitolo: \"" + title_and_authors + "\"")
                            add_book(conn, isbn, title, authors)
                            add_item(conn, isbn, title, authors, username, price)
                            context.bot.send_message(chat_id, "Il libro è stato aggiunto al database.")
                            return
                    
                        context.bot.send_message(chat_id, "Libro non trovato. Controlla di aver inserito correttamente l'ISBN.")
                    else:
                        context.bot.send_message(chat_id, "Si è verificato un problema nella lettura del database.")
                except Exception as e:
                    print(str(e))
                    context.bot.send_message(chat_id, "Prezzo non valido.")
            else:
                context.bot.send_message(chat_id, "ISBN non valido.")
        else:
            context.bot.send_message(chat_id, "Per poter vendere libri devi avere un username pubblico, in modo tale che gli altri utenti possano contattarti. Puoi comunque acquistare libri con il comando /cerca.")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /vendi <ISBN> <Prezzo>")
