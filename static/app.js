class App extends Component {
    // This custom HTML element will be the
    // first and only element inside <body />.
    constructor() {
        super();
        onAppReady(this);
    }

    ready() {
        if (page == "listing") {
            if (app.user && app.initData) {
                this.insertions.update();
            } else {
                sendAlert({
                    icon: 'error',
                    title: 'Effettua il login per poter vedere i tuoi annunci.'
                });
            }
        } else if (page == "new") {
            if (app.user && app.initData) {
                this.form.fadeIn();
            } else {
                sendAlert({
                    icon: 'error',
                    text: 'Effettua il login per poter aggiungere un libro.'
                });
            }
        }
    }
}


window.customElements.define('app-container', App);