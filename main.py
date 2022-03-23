# -*- coding: utf-8 -*-
import json
import telegram
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater
from bs4 import BeautifulSoup
import logging
import requests
import pandas as pd

from module.handlers import handlers

def main():
    TOKEN = 'TOKEN'
    bot=telegram.Bot(TOKEN)
    updater= Updater(TOKEN, use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    handlers(updater)
    updater.start_polling()

if __name__ == '__main__':
    main()