# —— Modules
from flask import Flask, request, render_template
from module.create_connection import create_connection
from module.shared import DB_PATH, error_message
from module.find import find
import json

# creating the flask app
app = Flask(__name__)


# —— API Routes
# • /
# serve the web app
@app.route('/')
def home():
    return render_template('index.html')

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
def search():
    # getting user input
    query = request.args.get('q')

    # creating connection
    conn = create_connection(DB_PATH)
    if not conn:
        # returning error message
        return respond({'message': error_message}, success = False)
    
    # querying the database
    rows = find(query, conn, "Market")
    # closing connection
    conn.close()
    # returning results
    return respond({'results': rows})


# —— Utils
def respond(data, success = True):
    data['success'] = success
    # 1. python dict to json string
    data = json.dumps(data)
    # 2. creating the response object
    response = app.response_class(data)
    # 3. adding some headers
    response.headers.add('Content-Type', 'application/json')
    # 4. CORS support
    # in order to access data from a browser,
    # the server must include this header
    response.headers.add('Access-Control-Allow-Origin', '*')
    # if you wish to restrict access, replace *
    # with your current frontend domain.
    return response


# —— Starting app
if __name__ == '__main__':
    app.run()