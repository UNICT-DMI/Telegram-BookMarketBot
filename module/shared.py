# Paths
DB_PATH = "data/bookmarket.db"

YAML_PATH = "config/settings.yaml"


# Error messages
DB_ERROR = "Si è verificato un problema nella lettura del database."

PRICE_ERROR = "Prezzo non valido."

USERNAME_ERROR = "Per poter vendere libri devi avere un username pubblico, in modo tale che gli altri utenti possano contattarti. Puoi comunque acquistare libri con il comando /cerca."

ISBN_ERROR = "ISBN non valido. Deve essere un numero di 10 o di 13 cifre."


# Command usage
REQUEST_USAGE = "Utilizzo comando: /richiedi <ISBN>; <Prezzo>; <Titolo>; <Autori> \n\nEs: /richiedi 9788864201795; 4.08; One Piece 1; Eiichiro Oda"

DELETE_USAGE = "Utilizzo comando: /elimina"

MY_BOOKS_USAGE = "Utilizzo comando: /libri"

SEARCH_USAGE = "Utilizzo comando: /cerca <txt>"

SELL_USAGE = "Utilizzo comando: /vendi <ISBN> <Prezzo>"

START_MESSAGE = "Ciao! Con questo bot puoi mettere in vendita i tuoi libri usati e comprare libri che altri colleghi non utilizzano più. Per maggiori informazioni utilizza il comando /help"


# Request
NEW_REQUEST = "new_request"

NEW_REQUEST_APPROVED = "new_request;Y;"

NEW_REQUEST_DECLINED = "new_request;N;"

REQUEST_SENT = "La richiesta è stata inoltrata agli admin. Grazie del supporto!"

REQUEST_ALREADY_SENT = "Hai già inviato una richiesta per questo libro. La tua richiesta è in elaborazione."

PENDING_REQUEST = "New Pending Request:\n"

ADMIN_REQUEST_ACCEPTED = "Richiesta accettata."

ADMIN_REQUEST_DECLINED = "Richiesta rifiutata."

USER_REQUEST_ACCEPTED = "La tua richiesta è stata accettata. Il libro è stato messo in vendita."

USER_REQUEST_DECLINED = "La tua richiesta è stata rifiutata. Controlla se i dati inseriti sono corretti e riprova."

CASCADE_REQUEST = "Richiesta accettata a cascata precedentemente."

BOOK_IS_PRESENT = "Il libro esiste già nel database locale. "

STATS_MESSAGE = "Il numero di libri in vendita in questo momento nel market è: "


# Other constant
NO = "N"

YES = "Y"

ISBN_PREFIX_1 = "978"

ISBN_PREFIX_2 = "979"

INSERT = "insert"

SELECT = "select"

FIND = "find"


# Delete
DELETE = "delete"

DELETE_APPROVED = 'delete;'

DELETING = "Eliminazione del libro selezionato..."

DELETED = "Libro eliminato."

SELECT_BOOK_TO_DELETE = "Quale libro vuoi eliminare?"

DELETE_UNAUTHORIZED = "L'username risulta diverso da quello del venitore originale."


# Books and Sales
ON_SALE_CONFIRM = "Il libro è stato messo in vendita."

LIST_BOOKS = "Hai i seguenti libri in vendita:\n"

NO_BOOKS = "Non hai libri in vendita."

BOOKS = "Books"

MARKET = "Market"

SEARCHING_ISBN = "Ricerca del libro associato all'ISBN inserito..."

SEARCH_RESULT = "La ricerca ha prodotto i seguenti risultati:\n"

NOTHING_FOUND = "Non ho trovato nulla."

BOOK_NOT_AVAILABLE = "Libro non trovato. Controlla di aver inserito correttamente l'ISBN. Se l'ISBN è corretto, utilizza il comando /richiedi per fare una richiesta di inserimento manuale."


# Scraping
URL_1 = "https://catalogo.unict.it/search/i?SEARCH="

URL_2 = "&sortdropdown=-&searchscope=9"

NO_MATCHES = "No matches found"


# API error messages
INVALID_DATA = "Invalid data. Make sure you have set the Content-Type header to \"application/json\"."

MISSING_FIELD = lambda key: f"Missing {key} field in JSON body."

INVALID_FIELD = lambda key: f"Invalid field: {key}."