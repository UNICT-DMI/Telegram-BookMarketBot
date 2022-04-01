# Telegram-BookMarketBot
A Telegram Bot for UNICT students to sell and buy second hand university books

## How does it work?
The bot relies on a local database, in which two main tables are stored: `Books` and `Market`. Users can sell their books using the books' ISBN code.

If the book with that ISBN is present inside the `Books` table, the info about that book (like the book's name and authors) will be taken from there and then the on sale item will be added to the `Market` table, along with other information like the seller's username and the selling price of the book.

If the inserted ISBN is not present inside the local database, the bot will get the data from the UNICT Library Catalogue and then insert the retrieved info inside the `Books` table and then will add the new on sale item to the `Market` one.

Users that want to buy second hand books can look for them inside the market by doing a research, inserting the book's ISBN, title or author name as keyword. All the books matching the query will be displayed to the user, along with the usernames of their owners. In this way, people can contact sellers to make a deal in private.

Lastly, users can delete their on sale items from the database once they've been sold (or for any other reasons). It is of the seller's interest to delete their items once they are not on sale anymore: infact, people could contact them to buy a book that is present on the database even though they don't possess it or don't want to sell it.

## Testing
To test the bot follow these steps:
- Clone this repository
- Create `config/settings.yaml` (or copy the existing `config/settings.yaml.dist` and rename it into `config/settings.yaml`)
- Insert your Telegram Bot Token inside the file
- Copy `data/bookmarket.db.dist` and rename it into `data/bookmarket.db`
- Run `main.py` to start the bot
