class SearchBar extends HTMLElement {
    constructor() {
        super();
        this.setup();
    }

    setup() {
        this.input = document.getElementById('search-input');
        this.input.addEventListener('input', this.oninput.bind(this));
    }

    oninput(event) {
        // request the API
        // remember the current value
        let current = this.input.value;
        // prevent useless calls in case
        // the user is still typing
        setTimeout(() => {
            if (current != this.input.value) return;
            app.api.search(this.input.value, (response) => {
                // in case the user has typed some other
                // characters, don't display the
                // old search results, because they
                // may go over the correct ones.
                if (current != this.input.value) return;
    
                if (response.success) {
                    // update the UI
                    app.results.update(response.results);
                } else {
                    // display error message
                    alert('Error: ' + response.message);
                }
            });
        }, 500);
    }
}

window.customElements.define('search-bar', SearchBar);