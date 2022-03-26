import requests
from module.get_on_sale import get_on_sale
from module.find_book import find_book
from module.get_books import get_books
from bs4 import BeautifulSoup
import pandas as pd
from telegram import Update
from telegram.ext import CallbackContext
from module.shared import SHOP_DB_PATH, BOOKS_DB_PATH

def sell(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    if message!="/vendi":
        user_isbn = message.split()[1]
        try:
            format(float(message.split()[2].replace(',', '.')), '.2f')
            prezzo = str(format(float(message.split()[2].replace(',', '.')), '.2f'))
            username ="@"+str(context.bot.get_chat(chat_id)['username'])
            context.bot.send_message(chat_id, "Ricerca del libro associato all'ISBN inserito...")
            books = get_books()
            found, n = find_book(user_isbn, books)
            if found:
                isbn = str(books.iloc[n][0])
                title  = str(books.iloc[n][1])
                authors  = str(books.iloc[n][2])
                title_and_author  = title + "di" + authors
                context.bot.send_message(chat_id, "Il libro è: \nTitolo: \"" + title_and_author + "\"")
                df = get_on_sale()
                new_row = pd.DataFrame({'ISBN':str(isbn),'Titolo':str(title), 'Autori':str(authors), 'Venditore':str(username), 'Prezzo':str(prezzo)}, index=[len(df)])
                df = pd.concat([df, new_row])
                df.to_csv(SHOP_DB_PATH)
                context.bot.send_message(chat_id, "Il libro è stato aggiunto al database.")
            else:
                url="https://catalogo.unict.it/search/i?SEARCH=" + user_isbn + "&sortdropdown=-&searchscope=9"
                x = requests.get(url)
                soup = BeautifulSoup(x.content, 'html.parser')
                check = str(soup.findAll('td'))
                if "No matches found" not in check:
                    title_and_author  = soup.find('strong').text
                    context.bot.send_message(chat_id, "Il libro è: \nTitolo: \"" + title_and_author + "\"")
                    title  = soup.find('strong').text.split('/')[0]
                    authors  = soup.find('strong').text.split('/')[1]
                    isbn = str(soup.findAll('td')).split("bibInfoData")[len(str(soup.findAll('td')).split("bibInfoData"))-1].split("\n")[1].split("<")[0]
                    df = get_on_sale()
                    new_row = pd.DataFrame({'ISBN':str(isbn),'Titolo':str(title), 'Autori':str(authors), 'Venditore':str(username), 'Prezzo':str(prezzo)}, index=[len(df)])
                    df = pd.concat([df, new_row])
                    df.to_csv(SHOP_DB_PATH)
                    new_book = pd.DataFrame({'ISBN':str(isbn),'Titolo':str(title), 'Autori':str(authors)}, index=[len(books)])
                    books = pd.concat([books, new_book])
                    books.to_csv(BOOKS_DB_PATH)
                    context.bot.send_message(chat_id, "Il libro è stato aggiunto al database.")
                else:
                    context.bot.send_message(chat_id, "Libro non trovato. Controlla di aver inserito correttamente l'ISBN")
        except Exception as e:
            print(str(e))
            context.bot.send_message(chat_id, "Prezzo non valido")
    else:
        context.bot.send_message(chat_id, "Utilizzo comando: /vendi <ISBN> <Prezzo>")
