class BookResult extends HTMLElement {
    constructor() {
        super();
    
        // default book cover
        this.defaultCover = 'static/res/no-cover.png';

        this.setup();
    }

    setup() {
        // since the "BookResult" needs to be rendered
        // on the fly, it's not possible to declare
        // them in the index.html file, which is usually preferred
        this.cover = new Icon({src: this.defaultCover, size: window.innerWidth > 800 ? 200 : 100});
        this.info = document.createElement('book-info');
        this.base = document.createElement('book-base');
        this.price = document.createElement('book-price');
        this._title = document.createElement('book-title');
        this.author = document.createElement('book-author');
        this.seller = document.createElement('book-seller');
        this.link = document.createElement('a');

        this.seller.append(this.link);
        this.info.append(this._title, this.author, this.seller);
        this.base.append(this.cover, this.info);
        this.append(this.base);

        if (window.innerWidth < 800) {
            this.cover.append(this.price);
            // some style adjustments
            this.cover.style.width = 'fit-content';
            // this.cover.style.removeProperty('width');
            // this.cover.style.removeProperty('height');
        } else {
            this.append(this.price);
        }
    }

    update(data) {
        // Set book content.
        this.data = data;
        this._title.textContent = this.data[2];
        this.author.textContent = this.data[3];
        this.seller.textContent = 'Venduto da ';
        this.price.textContent = `€${this.data[5]}`;

        // creating a link to the seller
        let link = document.createElement('a');
        link.href = `https://t.me/${this.data[4].slice(1)}`;
        link.textContent = this.data[4];
        this.seller.append(link);

        // adding cover if provided
        this.cover.image.src = `https://syndetics.com/index.php?isbn=${this.data[1]}/mc.gif&client=cataniau&type=snui`;
        this.cover.image.onload = (function() {
            if (this.cover.image.naturalWidth == 1) {
                // image not found
                this.cover.image.src = this.defaultCover;
            }
        }).bind(this);
    }
}

window.customElements.define('book-result', BookResult);