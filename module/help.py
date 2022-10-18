from telegram import Update
from telegram.ext import CallbackContext


def help(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    vendi = "/vendi <ISBN> <Prezzo>: Aggiungi un libro alla lista degli oggetti in vendita. Inserisci l'ISBN del tuo libro e il prezzo con il quale lo vorresti vendere.\nEs: /vendi 9788890234484 17.50\n\n"
    cerca = "/cerca <txt>: Cerca un libro all'interno della lista degli oggetti in vendita. La ricerca si baserà su ciò che hai inserito successivamente al comando. All'interno dei risultati della ricerca sono presenti sia le informazioni sui libri sia il contatto della persona che l'ha messo in vendita.\nEs: /cerca modelli matematici\n\n"
    elimina = "/elimina: Elimina un libro che avevi precedentemente inserito nella lista degli oggetti in vendita. Puoi utilizzare questo comando, ad esempio, quando avrai venduto il tuo libro o se non vorrai più venderlo.\nEs: /elimina\n\n"
    libri = "/libri: Elenca i tuoi libri in vendita.\nEs: /libri"
    context.bot.send_message(chat_id, "Comandi disponibili:\n\n" + vendi + cerca + elimina + libri)
