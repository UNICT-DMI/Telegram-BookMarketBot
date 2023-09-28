from urllib.parse import unquote, parse_qsl
from flask import request
import hashlib, hmac, json
from routes.utils import app, respond
from module.shared import INVALID_DATA, MISSING_FIELD, INVALID_FIELD

"""
When opening the bot's WebApp on Telegram, or when logging in via Telegram on the website,
the received data about the user needs to be validated before using it on the server.
See https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app
Implementation taken from https://stackoverflow.com/questions/72044314/how-to-validate-data-received-via-the-telegrams-web-app
"""

def validate() -> bool:
    "Validates telegram data passed in the active flask request."
    if not request.json:
        return respond({'message': INVALID_DATA}, success = False)
    
    # Collecting parameters
    # init_data — the query string passed by the webapp
    init_data = request.json.get('init_data', None)
    if init_data is None:
        return respond({'message': MISSING_FIELD('init_data')}, success = False)
    # hash_str — the hash string passed by the webapp
    try: hash_str = dict(parse_qsl(init_data.replace('\n', '&')))['hash']
    except: return respond({'message': INVALID_FIELD('init_data')}, success = False)
    # web_app — whether data is coming from webapp or login widget
    web_app = request.json.get('web_app', False)

    # Validating data
    if web_app:
        init_data = sorted([
            chunk.split("=") \
            for chunk in unquote(init_data).split("&") \
            if chunk[:len("hash=")] != "hash="
        ], key = lambda x: x[0])
        init_data = "\n".join([f"{rec[0]}={rec[1]}" for rec in init_data])
        # https://core.telegram.org/bots/webapps#validating-data-received-via-the-mini-app
        secret_key = hmac.new(b"WebAppData", app.bot_token.encode(), hashlib.sha256).digest()
    else:
        start = init_data.find('hash')
        end = init_data.find('\n', start)
        init_data = init_data[:start] + init_data[end+1:]
        # https://core.telegram.org/widgets/login#checking-authorization
        secret_key = hashlib.sha256(app.bot_token.encode()).digest()
    data_check = hmac.new(secret_key, init_data.encode(), hashlib.sha256)
    if data_check.hexdigest() == hash_str:
        result = dict(parse_qsl(init_data.replace('\n', '&')))
        return json.loads(result['user']) if web_app else result
    else:
        # Verification failed!
        # logging.warn("Telegram initData verification failed.")
        return respond({"message": "Could not verify telegram data."}, success = False)