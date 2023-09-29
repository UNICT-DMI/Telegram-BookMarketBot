class BookPage extends Component {
    // Displays info and list of avaliable prices of a book.
    constructor() {
        super();
        this.offersTable = [];
    }

    update(book) {
        this.bookTitle.textContent = book.title;
        this.description.textContent = book.description;
        setImage(this.cover.image, book.cover);
        
        const offers = app.search.data.filter((e, i, _) => e.isbn == book.isbn);

        let i = 0;
        for (i; i < offers.length; i++) {
            if (this.offersTable[i]) {
                this.updateRow(this.offersTable[i], offers[i]);
            } else {
                let row = this.createRow();
                this.updateRow(row, offers[i]);
                this.offersTable.push(row);
            }
        }

        while (i < this.offersTable.length) {
            this.offersTable[i].style.display = 'none';
            i += 1;
        }
    }

    createRow() {
        const row = document.createElement('table-row');
        const price = document.createElement('row-price');
        const contact = document.createElement('a');
        // const conditions = document.createElement('row-conditions');
        row.append(price, contact); // , conditions);
        row.price = price;
        row.contact = contact;
        this.rows.append(row);

        // Final result
        /* <table-row>
            <row-price>20€</row-price>
            <a href = "https://t.me">@pincopallino</a>
            <row-conditions>ottime</row-conditions>
        </table-row> */
        return row;
    }

    updateRow(row, book) {
        row.price.textContent = "€" + book.price.toFixed(2);
        row.contact.textContent = book.seller;
        row.contact.href = `https://t.me/${book.seller.replaceAll("@", "")}`;
        // conditions.textContent = book.conditions || "sconosciute";
        row.style.display = 'flex';
    }
};

window.customElements.define('book-section', BookPage);