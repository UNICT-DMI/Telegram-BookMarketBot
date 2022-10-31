import bs4
from telegram import Update
from telegram.ext import CallbackContext
from module.add_item import add_item
from module.add_book import add_book
from module.find import find
from module.book_in_unict import book_in_unict
from module.create_connection import create_connection
from module.manage_requests import add_request, send_request
from module.send_results import get_book_info
from module.shared import DB_PATH, error_message


def _get_isbn_from_website(soup: bs4.BeautifulSoup) -> str:
    idx = len(str(soup.findAll("td")).split("bibInfoData")) - 1
    return str(soup.findAll("td")) \
        .split("bibInfoData")[idx] \
        .split("\n")[1] \
        .split("<")[0]


def request(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message == "/richiedi" or len(message.split('; ')) != 4:
        context.bot.send_message(chat_id, "Utilizzo comando: /richiedi <ISBN>; <Prezzo>; <Titolo>; <Autori>")
        return

    username = "@" + str(context.bot.get_chat(chat_id)["username"])
    if username.lower() == "@none":
        context.bot.send_message(chat_id, "Per poter eseguire questo comando devi avere un username pubblico.")
        return

    user_isbn = message.split('; ')[0].split()[1]
    if len(user_isbn) != 10 and len(user_isbn) != 13:
        context.bot.send_message(chat_id, "ISBN non valido. Deve essere un numero di 10 o di 13 cifre.")
        return
    
    try:
        format(float(message.split('; ')[1].replace(",", ".")), ".2f")
        price = str(format(float(message.split('; ')[1].replace(",", ".")), ".2f"))

        conn = create_connection(DB_PATH)
        if not conn:
            context.bot.send_message(chat_id, error_message)
            return

        rows = find(user_isbn, conn, "Books")
        conn.close()
        if rows:
            isbn, title, authors = rows[0]
            context.bot.send_message(chat_id, 'Il libro esiste già nel database locale:\n' + get_book_info(isbn, title, authors))
            add_item(isbn, title, authors, username, price)
            context.bot.send_message(chat_id, "Il libro è stato messo in vendita.")
            return

        found, soup = book_in_unict(user_isbn)
        if found:
            isbn = _get_isbn_from_website(soup)
            title = soup.find("strong").text.split("/")[0]
            authors = soup.find("strong").text.split("/")[1]
            context.bot.send_message(chat_id, 'Il libro esiste già nel database locale:\n' + get_book_info(isbn, title, authors))
            add_book(isbn, title, authors)
            add_item(isbn, title, authors, username, price)
            context.bot.send_message(chat_id, "Il libro è stato messo in vendita.")
            return

        title = message.split('; ')[2]
        authors = message.split('; ')[3]
        
        conn = create_connection(DB_PATH)
        if not conn:
            context.bot.send_message(chat_id, error_message)
            return
        cur = conn.cursor()
        cur.execute("SELECT * FROM Requests WHERE ISBN=? AND Seller=?", (user_isbn, username,))
        rows = cur.fetchall()
        
        if not rows:
            row_id = add_request(context, chat_id, user_isbn, title, authors, username, price)
            send_request(context, row_id)
            context.bot.send_message(chat_id, "La richiesta è stata inoltrata agli admin. Grazie del supporto!")
        else:
            context.bot.send_message(chat_id, "Hai già inviato una richiesta per questo libro. La tua richiesta è in elaborazione.")
        
    except Exception as e:
        print(str(e))
        context.bot.send_message(chat_id, "Prezzo non valido.")
