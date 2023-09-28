class Insertion extends Component {
    // Represents a user's published book.
    constructor() {
        super();

        // Creating elements
        this.info = document.createElement('insertion-info');
        this.icon = new Icon({tag: 'delete', color: 'ff3333', size: 35});
        this.cover = new Frame({src: "static/images/no-cover.png", width: vw() > 800 ? 100 : 50});
        this.book = document.createElement('insertion-book');
        this._title = document.createElement('insertion-title');
        this.authors = document.createElement('insertion-authors');
    }

    connectedCallback() {
        super.connectedCallback();
        // Defining structure
        this.append(this.info, this.icon);
        this.info.append(this.cover, this.book);
        this.book.append(this._title, this.authors);
        this.update(this.data);

        // Final result is something like this
        /* <insertion-data>
            <insertion-info>
                <image-frame name = "cover" src = "static/images/no-cover.png" width = 100></image-frame>
                <insertion-book>
                    <insertion-title>Book title</insertion-title>
                    <insertion-authors>Book authors</insertion-authors>
                </insertion-book>
            </insertion-info>
            <icon-container name = "delete" tag = "delete" color = "ff3333" size = 35></icon-container>
        </insertion-data> */

        // Event handler
        this.icon.onclick = (() => {
            sendConfirm({
                title: 'Eliminare questo annuncio?',
                showCancelButton: true,
                confirmButtonText: 'Sì, elimina',
            }, this.unpublish.bind(this))
        }).bind(this)
    }

    update(data) {
        // Filling data
        this.data = data;
        this._title.textContent = data.title;
        this.authors.textContent = data.description;
        setImage(this.cover.image, getCoverUrl(data.isbn));
        this.show();
    }
    
    unpublish() {
        // Remove currently displaying insertion from the database
        app.api.call('delete', {insertion_id: this.data.insertion_id}, ((response) => {
            if (!response.success) {
                // Something went wrong.
                sendAlert({icon: 'error', title: 'Errore', text: response.message});
            } else {
                // Hiding the deleted insertion.
                this.style.display = 'none';
                // Removing it from the list
                this.removeFromList();
            }
        }).bind(this));
    }

    removeFromList() {
        let index = this.parentNode.insertions.indexOf(this);
        if (index != -1) {
            this.parentNode.insertions.splice(index, 1);
            // Avoiding a blank screen
            // if there are no more books
            if (this.parentNode.insertions.length == 0) {
                app.home.enterFromRight(true);
            }
        }
    }
};


window.customElements.define('insertion-data', Insertion);