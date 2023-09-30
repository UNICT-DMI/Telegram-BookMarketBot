// Functions used here and there
// Get current viewport width and height
const vw = () => Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)
const vh = () => Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)


// Get CSS variables
function getCSSVariable(key) {
    return getComputedStyle(document.documentElement).getPropertyValue(key);
}

// Get a book's cover from ISBN
function getCoverUrl(isbn) {
    // return `https://syndetics.com/index.php?isbn=${isbn}/mc.gif&client=cataniau&type=snui`;
    // ↑ low quality
    return `https://www.lafeltrinelli.it/images/${isbn}_0_536_0_75.jpg`;
}

function setImage(image, source) {
    image.src = source;
    // Replace image with the default cover in case it couldn't be found.
    image.onload = () => {
        if (image.naturalWidth == 536 && image.naturalHeight == 536 || image.naturalWidth == 0) {
            // Rendered image is probably the "missing cover" from Feltrinelli
            // replacing it with BookMarket's which fits better
            image.src = constants.defaultCover;
        }
    };

    image.onerror = () => {
        image.src = constants.defaultCover;
    }
}


function sendAlert(options) {
    if (window.Telegram.WebApp.initData) {
        // Preferring telegram native popup
        window.Telegram.WebApp.showAlert(`${options.title ? options.title + ": " : ""}${options.text}`);
    } else {
        try {Swal.fire(options)}
        catch (ReferenceError) {setTimeout(sendAlert.bind(options, 1000))}
    }
}

function sendConfirm(options, onConfirm) {
    if (window.Telegram.WebApp.initData) {
        window.Telegram.WebApp.showConfirm(options.title, (confirm) => {
            if (confirm) {
                onConfirm();
            }
        });
    } else {
        Swal.fire(options).then((result) => {
            if (result.isConfirmed) {
                onConfirm();
            }
        })
    }
}

// Other constants
const constants = {
    defaultCover: "static/images/no-cover.png",
    botUsername: "BookMarketTestBot"
};


// Things to do before submitting:
// - changing telegram widget bot username
// - changing username here
// - /setdomain instructions