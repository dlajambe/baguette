import logging

from modules.logger import initialize_logger
from config import Config

def train_model():
    initialize_logger('train_model', Config.log_root)
    logging.info('Beginning train_model.py')

if __name__ == '__main__':
    try:
        train_model()
    except Exception as ex:
        logging.exception(ex)
