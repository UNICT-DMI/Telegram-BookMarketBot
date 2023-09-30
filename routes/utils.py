from flask import current_app as app
import json


def respond(data: dict, success: bool = True):
    "Respond to a flask request with JSON."
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
    # to restrict access, replace * with
    # your current frontend domain.
    return response