class Page extends Component {
    constructor() {
        super();
    }

    connectedCallback() {
        super.connectedCallback();
        // adding the "page" class
        this.classList.add('page');

        // add this to the list of pages
        if (!app.pages) app.pages = [];
        app.pages.push(this);

        // if there is no page active, activate this one
        if (!app.currentPage) {
            app.currentPage = this;
        } else {
            this.hide();
        }
    }

    fadeIn() {
        // 1. Fade out the current page
        app.currentPage.classList.add('fade-out');
        setTimeout((() => {
            // 2. Show this one but with opacity set to 0%
            this.classList.add('prepare-to-show');
            // 3. Completely hide the previous one (display: none)
            app.currentPage.hide();
            // 4. Start to show this one progressively
            this.classList.add('fade-in');
            setTimeout((() => {
                // 5. Completely show this one (display: flex)
                this.show();
                // 6. Clean previously set classes
                this.classList.remove('prepare-to-show', 'fade-in');
                app.currentPage.classList.remove('fade-out');
                // 7. Set global current active page to this
                app.currentPage = this;
            }).bind(this), this.animationTime);
        }).bind(this), this.animationTime);
    }

    enterFromRight(reverse) {
        // 1. Slide to left the current page
        app.currentPage.classList.add('slide-' + (reverse ? 'right' : 'left'));
        // 2. Put this page on the right
        this.classList.add('stop-animations');
        this.classList.add('slide-' + (reverse ? 'left' : 'right'));
        this.classList.add('prepare-to-show');
        // 3. Slide this page from the right
        setTimeout((() => {
            // 4. Completely hide the previous one (display: none)
            if (!reverse) app.currentPage.hide();

            this.classList.remove('stop-animations', 'slide-' + (reverse ? 'left' : 'right'));
            this.classList.add('fade-in');
            setTimeout((() => {
                if (reverse) app.currentPage.hide();
                // 5. Completely show this one (display: flex)
                this.show();
                // 6. Clean previously set classes
                this.classList.remove('fade-in', 'slide-' + (reverse ? 'left' : 'right'), 'prepare-to-show');
                app.currentPage.classList.remove('slide-' + (reverse ? 'right' : 'left'));
                // 7. Set global current active page to this
                app.currentPage = this;
            }).bind(this), this.animationTime);
        }).bind(this));
    }


    get animationTime() {
        return parseInt(this.getVariable('--animation-time'));
    }
}


window.customElements.define('base-page', Page);