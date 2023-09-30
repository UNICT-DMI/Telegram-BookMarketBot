class Frame extends Component {
    constructor(options = {}) {
        // Main component for displaying images and icons.
        super();
        
        /* Options must include
        :width: image's width
        :height: image's height
        :src: the img element's source
        
        Options can also be passed as HTML attributes
        <image-frame size = "12" src = "..."> */
        this.options = options;
        this.setup();
    }

    setup() {
        // creating the image element
        this.image = document.createElement('img');
    }

    connectedCallback() {
        super.connectedCallback();
        this.classList.add('image-frame');
        this.append(this.image);
        this.image.src = this.src;


        let width = this.width + 'px';
        let height = this.height + 'px';
        this.setVariable('--width', width);
        this.setVariable('--height', height);
    }

    get width() {
        return parseFloat(this.options.width || this.getAttribute('width') || this.options.size || this.getAttribute('size'));
    }

    get height() {
        return parseFloat(this.options.height || this.getAttribute('height') || this.options.size || this.getAttribute('size'));
    }

    get src() {
        return this.options.src || this.getAttribute('src');
    }
}


window.customElements.define('image-frame', Frame);