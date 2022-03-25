# -*- coding: utf-8 -*-
from telegram.ext import Updater
import logging

from module.handlers import handlers

def main() -> None:
    TOKEN = '1739559917:AAEg2DwAEB2k5CmFUv4T1HuqBh2E3-Sj6go'
    updater= Updater(TOKEN, use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    handlers(updater)
    updater.start_polling()

if __name__ == '__main__':
    main()