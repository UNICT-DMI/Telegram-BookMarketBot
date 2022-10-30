# -*- coding: utf-8 -*-
from telegram.ext import Updater
import logging, yaml
from module.handlers import handlers
from app import app


def main() -> None:
    with open('config/settings.yaml', 'r') as yaml_config:
        config_map = yaml.load(yaml_config, Loader=yaml.SafeLoader)
    updater= Updater(config_map['token'], use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    handlers(updater)

    updater.start_polling()
    app.run()


if __name__ == '__main__':
    main()
