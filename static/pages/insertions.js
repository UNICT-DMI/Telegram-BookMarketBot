class InsertionsPage extends Page {
    constructor() {
        super();
        this.insertions = [];
    }

    // Lists the user's active insertions.
    update() {
        app.api.call('list', {}, (data) => {
            if (!data.success) {
                // Something went wrong.
                return sendAlert({icon: 'error', title: 'Errore', text: data.message});
            }
            
            if (data.result.length == 0) {
                // The user has no active insertions.
                sendAlert({icon: 'info', text: 'Non hai libri in vendita.'});
            } else {
                const books = app.api.formatBooks(data.result);
                for (var i=0; i < books.length; i++) {
                    // If there is already an "insertion" element, update it
                    if (this.insertions[i]) {
                        this.insertions[i].update(books[i]);
                    } else {
                        // otherwise, create a new one
                        let insertion = new Insertion();
                        insertion.update(books[i]);
                        this.insertions.push(insertion);
                        this.append(insertion);
                    }
                }

                while (i < this.insertions.length) {
                    this.insertions[i].hide();
                    i += 1;
                }
                
                this.fadeIn();
            }
        });
    }
};


window.customElements.define('insertions-page', InsertionsPage);