import logging
import random

logging.basicConfig(filename="joy.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
)

for i in range(0,15):
    if (i%2==0):
        logging.warning('Log warning Message')
    elif (i%3==0):
        logging.critical('Log critical Message')
    else:
        logging.error('Log error Message')

