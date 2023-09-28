// Makes the website available as a progressive web app.
document.addEventListener('DOMContentLoaded', () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js', {scope: '/'}).catch(function(err) {
            console.warn('Error whilst registering service worker', err);
        });
    }

    // colors.setStatusBar('#' + colors.get('--background-color'));
    // window.addEventListener('online', (e) {}, false);
    // window.addEventListener('offline', (e) => {}, false);
});