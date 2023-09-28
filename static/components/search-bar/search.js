class SearchBar extends Component {
    constructor() {
        super();
        this.shelf = document.getElementsByTagName('book-case');
    }

    oninput(bar) {
        const query = bar.value;
        // Trigger actual search process if
        // query doesn't change for a few seconds
        // (which means the user has stopped typing)
        setTimeout(() => {
            if (query == bar.value) {
                this.search(query);
            }
        }, 1000);

        // Hiding website instructions
        app.instructions.classList.add('faded');
    }

    search(query) {
        // In case page is not visible
        app.home.enterFromRight(true);
        
        // Searching books
        fetch(`search?q=${query}`)
         .then((response) => response.json())
         .then((data) => {
            const books = app.api.formatBooks(data.results);
            this.update(books);
         });
    }

    update(books) {
        this.data = books;
        if (books.length == 0) {
            // No books found.
            app.noResults.show();
            for (let j = 0; j < this.shelf.length; j++) {
                this.shelf[j].hide();
            }

        } else {
            app.noResults.hide();
            // Filtering the list of results to remove
            // duplicates. The various offers will
            // be shown later, when clicking on the book.
            books = this.removeDuplicates(books);
            // Displaying results
            this.displayResults(books);
            app.instructions.hide();
            
            // Hiding unused components
            for (let j = books.length; j < this.shelf.length; j++) {
                this.shelf[j].hide();
            }
        }
    }


    removeDuplicates(books) {
        this.prices = {};
        return books.filter((book) => {
            const result = !this.prices[book.isbn];
            if (book.price < (this.prices[book.isbn] || book.price + 1.0)) {
                this.prices[book.isbn] = book.price;
            }

            return result;
        })
    }

    displayResults(books, count = 0) {
        if (count < books.length) {
            this.shelf[count].update({...books[count], price: this.prices[books[count].isbn]});
            setTimeout(this.displayResults.bind(this, books, count + 1), 300);
        }
    }
};

window.customElements.define('search-bar', SearchBar);