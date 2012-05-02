import logging
from ThoughtXplore.CONFIG import LOGGER_MENU


def MenuExceptionLog(fnx_name,msg,args={}):
    try:
        logging.basicConfig(level=logging.DEBUG)
        logger_exception = logging.getLogger(LOGGER_MENU)
        logger_exception.debug('[%s]%s || args=%s' % ( fnx_name,msg,str(args)))
    except:
        print 'exceptions in exptionlog'
        
def MenuInfoLog(fnx_name,message):
    try:
        logger_exception = logging.getLogger(LOGGER_MENU)
        logger_exception.info('[%s] %s' % ( fnx_name,message))
    except:
        print 'exceptions in MenuInfoLog'