// Starting point of the website.
const app = document.getElementsByTagName('app-container')[0];
// components will be stored as "app" attributes
// not to have more global variables
app.header = app.getElementsByTagName('app-header')[0];
app.search = app.getElementsByTagName('search-bar')[0];
app.results = app.getElementsByTagName('search-results')[0];
// other stuff
app.colors = new Colors();
app.api = new API();