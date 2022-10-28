class Colors {
    constructor() {
        this.defaultSettings = {
            bg_color: '#ffffff',
            text_color: '#000000',
            hint_color: '#f0f0f0',
            link_color: '#0000aa',
            button_color: '#0000aa',
            button_text_color: '#ffffff',
            secondary_bg_color: '#a0a0a0',
        }
    }

    get(key) {
        key += '_color';
        // Get the color used for a particular category
        // if the website is running via Telegram WebApps,
        // the result will match user's chosen theme.
        let color = window.Telegram.WebApp.themeParams[key] || this.defaultSettings[key];
        // removing the inital hashtag
        return color.slice(1, undefined);
    }
}