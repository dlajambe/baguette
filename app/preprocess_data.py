import logging
import pandas as pd

from modules.logger import initialize_logger
from config import Config

def preprocess_data():
    initialize_logger('preprocess_data', Config.log_root)
    logging.info('Beginning preprocess_data.py')
    logging.info('Loading data')

    chunk_idx = 1
    for chunk in pd.read_csv(Config.data_path_raw, chunksize=Config.chunk_size):
        print(chunk_idx)
        chunk_idx += 1
    
    logging.info('Preprocessing data')

if __name__ == '__main__':
    try:
        preprocess_data()
    except Exception as ex:
        logging.exception(ex)
