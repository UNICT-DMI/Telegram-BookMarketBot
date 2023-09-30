class Component extends HTMLElement {
    constructor() {
        // Base class for all components.
        super();
    }

    connectedCallback() {
        this.classList.add('component');
        // saving this component as an
        // attribute of the parent node
        this.name = this.getAttribute('name');
        if (this.name) {
            // this.parentNode[this.name] = this;
            // in some cases we may want this component
            // to be accessible not only from the parent
            let parent = this.parentNode;
            while (parent != null) {
                // we give the attribute to all the parents'
                parent[this.name] = this;
                parent = parent.parentNode;
                /* if (parent.onChildReady) {
                    parent.onChildReady(this);
                } if (parent.childComponents) {
                    parent.childComponents.push(this);
                } else {
                    parent.childComponents = [this];
                } */
            }
        }
    }

    setVariable(key, value) {
        // Sets the CSS variable for this component.
        this.style.setProperty(key, value);
    }

    getVariable(key) {
        // Returns the CSS variable.
        return getComputedStyle(this).getPropertyValue(key);
    }

    show() {
        this.classList.remove('hidden');
    }

    hide() {
        this.classList.add('hidden');
    }
}


window.customElements.define('base-component', Component);