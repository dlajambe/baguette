import logging
import logging.handlers
import os
from datetime import date

def initialize_logger(log_prefix:str, log_root: str) -> None:
    """Initializes and configures the logger with a console and file 
    sink.

    A new log file is generated every time this function is called with
    the following naming convention:

    {log_prefix}_YYYY_MM_DD.{log_idx}.log

    Parameters
    ----------
    log_prefix : str
        The prefix that should be added to the file log name.

    log_root : str
        The root directory in which log files should be stored.
    """

    # Step 1 - Create the required log directories if they do not
    # already exist
    if os.path.exists(log_root) == False:
        os.mkdir(log_root)
    
    log_dir = os.path.join(log_root, log_prefix)
    if os.path.exists(log_dir) == False:
        os.mkdir(log_dir)
    
    # Step 2 - Generate a unique filename
    today = date.today()
    filename_base = log_prefix + "_" + date.strftime(today, '%Y_%m_%d') + '.'
    
    log_idx = 1
    filename_full = filename_base + str(log_idx) + '.log'
    filepath = os.path.join(log_dir, filename_full)
    while os.path.exists(filepath):
        log_idx += 1
        filename_full = filename_base + str(log_idx) + '.log'
        filepath = os.path.join(log_dir, filename_full)
    
    # Step 3 - Initialize the handlers and configure the logger
    file_handler = logging.FileHandler(filepath)
    console_handler = logging.StreamHandler()

    logging.basicConfig(
        handlers=[file_handler, console_handler],
        level=logging.DEBUG,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    
    logging.info('Logger successfully initialized')
    logging.info('File logger path: {}'.format(filepath))

    