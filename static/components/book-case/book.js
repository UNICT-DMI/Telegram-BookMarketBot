class BookCase extends Component {
    constructor() {
        super();
    }

    connectedCallback() {
        super.connectedCallback();
        this.addEventListener('click', this.onclick.bind(this));
        // Hiding for now. It will be shown when searching for books.
        this.hide();
    }

    update(data) {
        this.data = data;
        this.name.textContent = this.trim(data.title);
        this.description.textContent = this.trim(data.description);
        this.price.textContent = `a partire da €${data.price.toFixed(2)}`;
        setImage(this.cover.image, data.cover);

        this.show();
        setTimeout(() => {
            this.classList.add('updated');
        });
    }

    trim(text) {
        // Cuts a string after 50 characters on small screens.
        if (vw() > 800 || text.length <= 50) {
            return text;
        } else {
            return text.slice(0, 50) + '..';
        }
    }


    onclick(event) {
        app.bookDetails.update(this.data)
        app.bookPage.enterFromRight();
    }
};


window.customElements.define('book-case', BookCase);