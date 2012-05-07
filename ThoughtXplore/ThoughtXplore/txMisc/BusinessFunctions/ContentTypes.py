from ThoughtXplore.txMisc.models import MiscPermission, MiscState , PermissionContentType ,StateContentType
from django.contrib.contenttypes.models import ContentType
from ThoughtXplore.CONFIG import LOGGER_MISC
import logging



class ContentTypeClass():
    def __init__(self):
        self.MiscLogger = logging.getLogger(LOGGER_MISC)
    
    
    def getAllContentTypes(self):
        try:
            contenttypes_list = ContentType.objects.all()
            self.MiscLogger.debug("[%s] length of contenttypes_list is %s"%('getAllContentTypes',str(len(contenttypes_list))))
            return (1,contenttypes_list)
        except:
            self.MiscLogger.exception('[%s] == Exception =='%('getAllContentTypes'))
            return (-1,[])
    
    def getContentTypesByAppLabel(self,app_label_t):
         try:
            contenttypes_list = ContentType.objects.filter(app_label__exact = app_label_t)
            self.MiscLogger.debug("[%s] length of contenttypes_list is %s"%('getContentTypesByAppLabel',str(len(contenttypes_list))))
            return (1,contenttypes_list)
         except:
            self.MiscLogger.exception('[%s] == Exception == label req = %s'%('getContentTypesByAppLabel',app_label_t))
            return (-1,[])
