// Interact with the backend.
class API {
    search(query, callback) {
        // search a book and return JSON response
        fetch(`search?q=${query}`)
         .then((response) => response.json())
         .then((data) => callback(data));
    }
}