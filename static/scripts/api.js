class API {
    // Handles requests to the backend.
    constructor() {
        this.options = (params = {}) => ({
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                init_data: app.initData,
                web_app: window.Telegram.WebApp.initData ? true : false,
                ...params
            })
        });
    }

    call(endpoint, params, callback) {
        fetch(endpoint, this.options(params))
        .then((response) => response.json())
        .then((data) => callback(data));
    }


    formatBooks(data) {
        return data.map((raw) => ({
            isbn: raw[1],
            title: raw[2],
            description: raw[3],
            seller: raw[4],
            price: parseFloat(raw[5]),
            cover: getCoverUrl(raw[1]),
            insertion_id: raw[0]
        }));
    }
};


app.api = new API();