class Results extends HTMLElement {
    constructor() {
        super();
        this.setup();
    }

    setup() {
        this.books = [];
    }

    update(results) {
        // Display search results
        this.index = 0;
        for (var i=0; i < Math.min(results.length, 20); i++) {
            // keep adding books as long as they're available
            this.add(results[i]);
        }

        // there may be unwanted remaining books,
        // for example from a previous search
        // query that had more results than this one;
        // in this case, hide them
        while (i < this.books.length) {
            this.books[i].style.display = 'none';
            i += 1;
        }
    }

    add(data) {
        // Add book to the list
        let book;
        if (this.books[this.index]) {
            // if there's an element ready,
            // no need to create a new one
            book = this.books[this.index];
        } else {
            // creating a new book
            book = new BookResult();
            this.books.push(book);
            this.append(book);
        }
        
        // updating book info and index
        book.style.display = 'flex';
        book.update(data);
        this.index += 1;
    }
}

window.customElements.define('search-results', Results);