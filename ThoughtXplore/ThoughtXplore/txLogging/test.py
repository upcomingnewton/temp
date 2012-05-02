import logging
import logging.config
from ThoughtXplore.settings import LOGGING
# make loggers




#logger = logging.getLogger('simple_example')
#print logger
#logger.setLevel(logging.WARN)

# create a console handler
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)

#create formatter
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to handler
#ch.setFormatter(formatter)

# add handler to logger
#logger.addHandler(ch)

#application code
def test():
    logger = logging.getLogger('simpleExample')
    print logger
    logger.debug('debug message testing from settings')
    logger.info('info message testing from settings')
    logger.warn('warning testing from settings')
    logger.error('error testing from settings')
    logger.critical('critical testing from settings')