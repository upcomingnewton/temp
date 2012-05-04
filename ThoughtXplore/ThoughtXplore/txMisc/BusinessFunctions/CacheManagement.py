from django.core.cache import cache
from ThoughtXplore.CONFIG import LOGGER_MISC, CACHE_TIME_FOR_SECURITY, CACHE_CONTENTTYPES
import logging

LoggerMisc = logging.getLogger(LOGGER_MISC)


def getContentTypesFromCache():
    try:
        if cache.get(CACHE_CONTENTTYPES) is None:
            return (-1,[])
        else:
            return (1,cache.get(CACHE_CONTENTTYPES))
    except:
        LoggerMisc.exception('[%s] Exception'%('getContentTypesFromCache'))
        return (-1,[]) 
    
    
def setContentTypesForCache(content_type_list):
    try:
        if cache.get(CACHE_CONTENTTYPES) is not None:
            cache.delete(CACHE_CONTENTTYPES)
        cache.add(CACHE_CONTENTTYPES,content_type_list,CACHE_TIME_FOR_SECURITY)
        return 1
    except:
        LoggerMisc.exception('[%s] Exception'%('getContentTypesFromCache'))
        return -1