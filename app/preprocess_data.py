import logging
import pandas as pd

from modules.logger import initialize_logger
from config import Config
from spacy.lang.en import English

def preprocess_data():
    initialize_logger('preprocess_data', Config.log_root)
    logging.info('Beginning preprocess_data.py')
    logging.info('Loading data')
    tokenizer = English().tokenizer

    chunk_idx = 1
    for chunk in pd.read_csv(Config.data_path_raw, chunksize=1):

        chunk_idx += 1
        chunk_en = chunk['en'].iloc[0]
        doc = tokenizer(chunk_en)
        tokens = [token.text for token in doc]
        print('Raw: {}\tTokenized: {}'.format(chunk_en, tokens))

        if chunk_idx > 10:
            print(type(tokens))
            break    
    
    logging.info('Preprocessing data')

if __name__ == '__main__':
    try:
        preprocess_data()
    except Exception as ex:
        logging.exception(ex)
