import logging

from modules.logger import initialize_logger
from config import Config

def main():
    initialize_logger('train_model', Config.log_root)

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logging.exception(ex)
