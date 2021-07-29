import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s%(levelname)s:%(message)s')

logging.debug('This message will be ignored') # this will not get printed

logging.info('This should be logged') # This will get printed

logging.warning('Add this,too') # It'll print




