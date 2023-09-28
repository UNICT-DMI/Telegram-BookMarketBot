class Colors {
    // Handles all the color/theme-related things.
    constructor(app) {
        // keeping a reference to all the icons
        // to be able to change their colors when switching theme
        this.icons = [];
        // setting the status bar color
        const backgroundColor = this.get('--background-color', {includeHashtag: true});
        this.setStatusBar(backgroundColor);
        // setting accent color
        const buttonColor = this.get('--tg-theme-button-color');
        if (buttonColor) {
            this.set('--accent-color', this.rgb(buttonColor));
        }
    }

    get(key, options = {}) {
        // Get colors stored in CSS variables
        let color = getCSSVariable(key).trim();
        if (color.includes(',') && !options.rgb) color = this.hex(color);
        return (options.includeHashtag ? color : color.replace('#', ''));
    }

    set(key, color) {
        // Set colors stored in CSS variables
        document.documentElement.style.setProperty(key, color);
    }

    hex(rgb) {
        // Transform a color from RGB to HEX format
        rgb = rgb.match(/\d+/g);
        return "" + ((1 << 24) + (parseInt(rgb[0]) << 16) + (parseInt(rgb[1]) << 8) + parseInt(rgb[2])).toString(16).slice(1);
    }

    rgb(hex) {
        // Transform a color from HEX to RGB format
        var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}`;
    }

    setStatusBar(color) {
        // In android and windows standalone PWA,
        // set the color of the status bar
        document
            .getElementsByTagName('meta')
            .namedItem('theme-color')
            .setAttribute('content', color);
    }

    changeTheme(event) {
        // changing all the colors of HTML elements
        const theme = event.currentTarget.id.split('-')[0];
        document.documentElement.className = theme;
        // and of icons
        const color = this.get('--text-color');
        this.icons.forEach((icon) => {
            icon.color = color;
        });
    }
}


// Setting up a global variable so that
// every component can access it
const colors = new Colors();