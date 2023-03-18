from telegram import Update
from telegram.ext import CallbackContext

# pylint: disable=redefined-builtin
def help(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    sell = "/vendi <ISBN> <Prezzo>\nAggiungi un libro alla lista degli oggetti in vendita. Inserisci l'ISBN del tuo libro e il prezzo con il quale lo vorresti vendere.\nEs: /vendi 9788891296566 5.50\n\n"
    search = "/cerca <txt>\nCerca un libro all'interno della lista degli oggetti in vendita. La ricerca si baserà su ciò che hai inserito successivamente al comando. All'interno dei risultati della ricerca sono presenti sia le informazioni sui libri sia il contatto della persona che l'ha messo in vendita.\nEs: /cerca modelli matematici\n\n"
    delete = "/elimina\nElimina un libro che avevi precedentemente inserito nella lista degli oggetti in vendita. Puoi utilizzare questo comando, ad esempio, quando avrai venduto il tuo libro o se non vorrai più venderlo.\nEs: /elimina\n\n"
    books = "/libri\nElenca i tuoi libri in vendita.\nEs: /libri\n\n"
    request = "/richiedi <ISBN>; <Prezzo>; <Titolo>; <Autori>\nRichiedi l'inserimento manuale di un libro non presente nei database locali e/o online. Un admin controllerà la tua richiesta e aggiungerà manualmente il libro agli altri oggetti in vendita.\nNota bene: ogni campo deve essere separato dal carattere ';' seguito da uno spazio.\nEs: /richiedi 9788864201795; 4.08; One Piece 1; Eiichiro Oda\n\n"
    stats = "/stats\nRestituisce il numero di libri in vendita al momento nel market"
    context.bot.send_message(chat_id, "Comandi disponibili:\n\n" + sell + search + delete + books + request + stats)
