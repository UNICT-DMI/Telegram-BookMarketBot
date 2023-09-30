class FormPage extends Page {
    submit() {
        // Getting a reference to the inputs
        if (!this.isbnInput || !this.priceInput) {
            this.isbnInput = document.getElementById('form-isbn');
            this.priceInput = document.getElementById('form-price');
        }
        
        // Getting current input values
        const isbn = this.isbnInput.value;
        const price = this.priceInput.valueAsNumber;

        // Adding book to the database
        app.api.call('sell', {isbn: isbn, price: price}, (result) => {
            if (result.success) {
                // Done! Notify the user
                sendAlert({
                    icon: 'success',
                    title: 'Operazione eseguita',
                    text: `Il libro "${result.title}" di ${result.authors} è stato messo in vendita.`
                });

                // Switch page (?)
                app.home.enterFromRight(true);
                
                // Resetting values
                this.isbnInput.value = "";
                this.priceInput.value = "";
                app.form.cover.image.src = "";
            } else {
                // Something went wrong.
                sendAlert({
                    icon: 'error',
                    title: 'Errore',
                    text: result.message
                });
            }
        });
    }
}

window.customElements.define('form-page', FormPage);