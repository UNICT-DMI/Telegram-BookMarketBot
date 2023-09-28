// Login with Telegram can be done in three ways:
document.addEventListener('DOMContentLoaded', () => {
    // 1. If the app is running via Telegram WebApp,
    // the user shouldn't need to log in again
    if (window.Telegram.WebApp.initData) {
        // The client-side will update according to initDataUnsafe
        onTelegramAuth(window.Telegram.WebApp.initDataUnsafe.user);
        // later, server calls will include initData for validation
        app.initData = window.Telegram.WebApp.initData;
    }

    // 2. If the user has logged in in the past,
    // there should be valid data in localStorage
    else {
        const stored = localStorage.getItem('user');
        const initdata = localStorage.getItem('initdata');
        if (stored && initdata) {
            // Again, storing init_data string for later validation
            app.initData = initdata;
            // and in the meantime, updating ui with what we have
            onTelegramAuth(JSON.parse(stored));
        }
    }

    // 3. Clicking on the "Login with Telegram" widget.
    // Nothing to do right now, just waiting for it
    app.ready();
});


function onTelegramAuth(user) {
    // Called when the user logs in with Telegram
    // Note: the user should have set a username to publish a book
    if (!user.username) {
        sendAlert({
            icon: 'error',
            title: 'Username non impostato',
            text: 'Per favore, imposta un username Telegram personale se vuoi pubblicare annunci, in modo da permettere agli altri di contattarti.'
        });
    } else {
        // Showing "add announcement" and "list announcements" buttons
        app.addBookButton.show();
        app.listBooksButton.show();
        // Removing the "login with Telegram" widget
        removeLoginWidget();
        // Storing user data
        app.user = user;
        app.initData = app.initData || generateInitData(user);
        // Adding to localStorage, so the next time
        // we won't have to login again
        localStorage.setItem('user', JSON.stringify(user));
        localStorage.setItem('initdata', app.initData);
    }
}

function removeLoginWidget() {
    // In some cases, the widget may not be on the DOM yet.
    const widget = document.getElementById(`telegram-login-${constants.botUsername}`);
    if (widget) {
        // There is, so we can hide it safely
        widget.style.display = 'none';
    } else {
        // It is probably still loading
        setTimeout(removeLoginWidget, 1000);
    }
}

function generateInitData(data) {
    var initData = "";
    // "Data-check-string is a concatenation of all received fields,
    // sorted in alphabetical order, in the format key=<value> with
    // a line feed character ('\n', 0x0A) used as separator – e.g.,
    // 'auth_date=<auth_date>\nfirst_name=<first_name>\nid=<id>\nusername=<username>'."
    const entries = Object.entries(data).sort((a, b) => a[0].localeCompare(b[0]));
    for(let i=0; i < entries.length; i++) {
        initData += `${entries[i][0]}=${entries[i][1]}\n`;
    }

    // removing the last "\n"
    return initData.slice(0, initData.length - 1);
}