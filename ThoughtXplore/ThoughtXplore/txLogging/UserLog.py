from ThoughtXplore.CONFIG import LOGGER_USER
import logging
import traceback

def UserDebugLog(msg,name_of_module):
    try:
        user_logger = logging.getLogger('logger_user')
        user_logger.debug('lolwa')
    except:
        traceback.print_exc()
        
def test_logger():
    for x in range(1,11):
        msg = 'this is message no %d'% x
        UserDebugLog(msg, 'test_logger')