# Telegram-BookMarketBot
A Telegram Bot for UNICT students to sell and buy second hand university books

## How does it work?
Users can sell their books, which then will be inserted inside a local database (the `on_sale.csv` file). If the info about the sold book are not present inside the `books_db.csv` file, the bot will get them from the UNICT Library Catalogue and then insert them inside the book database. 
Users can also look for a book inside the database. All the books matching the research will be displayed to the user, along with the usernames of the people that sells those books.
Lastly, users can delete one of their books from the database once it has been sold (or for any other reasons).

## Testing
Insert your Telegram Bot Token inside the yaml file in the config folder. If you want a clean start, `on_sale.csv` and `books_db.csv` should be empty except for the first row (where the columns' names are defined), so remember to delete those records. In that way you'll have a clean database of both sellers and books. Run 'main.py' to start the bot.
