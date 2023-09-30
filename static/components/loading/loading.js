class Loading extends HTMLElement {
    constructor() {
        super();
        this.setup();
    }

    setup() {
        /* <div class="loadingio-spinner-ripple-3aum7dvbzc9">
            <div class="ldio-1otly835buh">
                <div></div>
                <div></div>
            </div>
        </div> */
        let spinner = document.createElement('div');
        spinner.classList.add('loadingio-spinner-ripple-3aum7dvbzc9');
        let circle = document.createElement('div');
        circle.classList.add('ldio-1otly835buh');
        let child = document.createElement('div');
        let child1 = document.createElement('div');
        let child2 = document.createElement('div');
        child.append(child1, child2);
        circle.append(child);
        spinner.append(circle);
        this.append(spinner);
    }
}

window.customElements.define('loading-spinner', Loading);