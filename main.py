# -*- coding: utf-8 -*-
import logging
import yaml
from app import app
from telegram.ext import Updater
from module.handlers import handlers
from module.shared import YAML_PATH


def main() -> None:
    with open(YAML_PATH, 'r', encoding="utf-8") as yaml_config:
        config_map = yaml.load(yaml_config, Loader=yaml.SafeLoader)
    updater= Updater(config_map['token'], use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    handlers(updater)

    updater.start_polling()
    app.run(port=5000, host="0.0.0.0")


if __name__ == '__main__':
    main()
