class Icon extends Frame {
    constructor(options = {}) {
        // Main component for displaying icons.
        /* Available options
        :tag: icon name from icons8.com (required)
        :type: the name of icons8's style
        :color: icon color
        
        May also be passed as HTML attributes
        <icon-container tag = ".." /> */
        super();
        this.options = options;
    }

    setup() {
        super.setup();
        // saving itself in the global icons array
        colors.icons.push(this);
    }

    connectedCallback() {
        if (this.round) {
            this.style.background = 'var(--accent-color)';
            this.style.borderRadius = '50%';
            this.style.padding = '10px';
            this.options.width = this.size;
            this.options.height = this.size;
        }

        super.connectedCallback();
    }

    get src() {
        // Building the icons8.com image URL
        return `https://img.icons8.com/${this.type}/${this.size + 20}/${this.color}/${this.tag}.png`;
    }

    get tag() {
        return this.options.tag || this.getAttribute('tag') || 'question-mark';
    }

    get color() {
        const color = this.options.color || this.getAttribute('color') || colors.get('--text-color');
        return color[0] == '-' ? colors.get(color) : color;
    }

    get type() {
        return this.options.type || this.getAttribute('type') || 'material-rounded';
    }

    get round() {
        return this.options.round || this.getAttribute('round');
    }

    get size() {
        return this.width;
    }

    set color(color) {
        // Set the new color and update image
        this.options.color = color;
        this.image.src = this.src;
    }

    set tag(tag) {
        // Set the new tag and update image
        this.options.tag = tag;
        this.image.src = this.src;
    }

    set type(type) {
        // Set the new type and update image
        this.options.type = type;
        this.image.src = this.src;
    }
}


window.customElements.define('icon-container', Icon);