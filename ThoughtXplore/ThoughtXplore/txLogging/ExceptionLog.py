import logging
from ThoughtXplore.CONFIG import LOGGER_USER

def UserExceptionLog(ip,fun_name,args={}):
    try:
        logger_exception = logging.getLogger(LOGGER_USER)
        logger_exception.exception('[%s][%s]args=%s' % ( fun_name,str(ip),str(args)))
    except:
        print 'exceptions in exptionlog'
        
def UserErrorLog(ip,fun_name,message):
    try:
        logger_error = logging.getLogger(LOGGER_USER)
        logger_error.error('[%s][%s] %s' % ( fun_name,str(ip),message))
    except:
        print 'exceptions in exptionlog'