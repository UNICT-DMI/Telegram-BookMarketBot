# —— Modules
from flask import Flask, render_template, send_file  #pylint: disable=import-error
from routes.utils import respond
from routes.search import search
from routes.add_book import sell
from routes.my_books import mybooks
from routes.delete import delete

# creating the flask app
app = Flask(__name__)


# —— API Routes
# • /
# serve the web app
@app.route('/')
def home():
    return render_template('index.html', page = "home")

# • /listing
# list of books you are selling
@app.route('/listing')
def listing():
    return render_template('index.html', page = "listing")

# • /new
# add a book to the market
@app.route('/new')
def new():
    return render_template('index.html', page = "new")

# • /ping
# may be used to check the server
# status and/or response time
@app.route('/ping')
def ping():
    return respond({'message': 'pong'})

# • /search?q={}
# search books in the
# bot's local database
@app.route('/search')
def _search():
    return search()

# • /sell
# {isbn, price, init_data, web_app}
# search books in the
# bot's local database
@app.route('/sell', methods = ['POST'])
def _sell():
    return sell()

# • /list
# {init_data, web_app}
# returns user's list of insertions.
@app.route('/list', methods = ['POST'])
def _list():
    return mybooks()

# • /delete
# {init_data, web_app, insertion_id}
# remove an insertion by its row_id
@app.route('/delete', methods = ['POST'])
def _delete():
    return delete()


# • /favicon.ico
# serve the website favicon
@app.route('/favicon.ico')
def favicon():
    return send_file('static/web/favicon.ico')

# • /sw.js
# serve the service worker file (for PWAs)
@app.route('/sw.js')
def service_worker():
    return send_file('static/web/sw.js')

# • /manifest.json
# manifest file (for PWAs)
@app.route('/manifest.json')
def manifest():
    return send_file('static/web/manifest.json')



# —— Starting app
if __name__ == '__main__':
    app.run()
