class Icon extends HTMLElement {
    constructor(options = {}) {
        super();
        this.options = options;
        // icons are taken for free from icons8.com
        // unless a "src" parameter is provided
        this.url = "https://img.icons8.com/{style}/{size}/{color}/{name}.png";

        this.setup();
    }

    setup() {
        // —— Getting input values
        // pass these values inside options when
        // creating an instance or as tag attributes
        // examples
        //    → new Icon({src: "https://www.example.com/icon.png"});
        //    → <icon-container src = "https://www.example.com/icon.png"></icon-container>

        this.src = this.getAttribute('src') || this.options.src;
        // :src: the icon URL
        this.size = parseInt(this.getAttribute('size') || this.options.size);
        // :size: the size (in pixels) of the icon
        this.name = this.getAttribute('name') || this.options.name;
        // :name: the icons8 name of the icon, if no URL is provided
        this._style = this.getAttribute('style') || this.options.style || 'material';
        // :style: the icons8 style of the icon, if no URL is provided

        // —— Creating the actual icon
        // "this" is just the container
        this.image = document.createElement('img');
        this.append(this.image);

        // setting image source
        this.image.src = this.src || this.url
          .replace('{style}', this._style)
          .replace('{size}', this.size)
          .replace('{color}', app.colors.get('text'))
          .replace('{name}', this.name);
        
        // setting container size
        this.style.width = this.size + 'px';
        this.style.height = this.size + 'px';
    }
}

window.customElements.define('icon-container', Icon);