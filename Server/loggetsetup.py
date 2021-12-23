import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(message)s')
file_handler = logging.FileHandler('User.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger = logging.getLogger()
logger.info('Started Log')
logger.info('----------------------')