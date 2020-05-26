'''
12.9 エラーメッセージのロギング
'''

import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', filename='blue_ox.log', format=fmt)

logger = logging.getLogger('bunyan')

logger.debug("Look like rain")

logger.info("And hail")

logger.warn("Did I hear thunder?")

logger.error("Was that lightning")

logger.critical("Stop fencing and get inside!")

