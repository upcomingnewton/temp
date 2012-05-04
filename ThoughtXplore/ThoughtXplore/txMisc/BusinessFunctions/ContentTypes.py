from ThoughtXplore.txMisc.models import MiscPermission, MiscState , PermissionContentType ,StateContentType
from django.contrib.contenttypes.models import ContentType
from ThoughtXplore.CONFIG import LOGGER_USER
import logging
from butterfly.aliasing import logger


class MiscFunctions():
    def __init__(self):
        self.UserLogger = logging.getLogger(LOGGER_USER)
    
    
    def getAllContentTypes(self):
        try:
            contenttypes_list = ContentType.objects.all()
            self.UserLogger.debug("[%s] length of contenttypes_list is %s"%('getAllContentTypes',str(len(contenttypes_list))))
            return (1,contenttypes_list)
        except:
            self.UserLogger.exception('[%s] == Exception =='%('getAllContentTypes'))
            return (-1,[])
    
    def getContentTypesByAppLabel(self,app_label_t):
         try:
            contenttypes_list = ContentType.objects.filter(app_label__exact = app_label_t)
            self.UserLogger.debug("[%s] length of contenttypes_list is %s"%('getContentTypesByAppLabel',str(len(contenttypes_list))))
            return (1,contenttypes_list)
         except:
            self.UserLogger.exception('[%s] == Exception == label req = %s'%('getContentTypesByAppLabel',app_label_t))
            return (-1,[])
        
    def getAllStates(self):
        try:
            states_list = MiscState.objects.all()
            self.UserLogger.debug("[%s] length of contenttypes_list is %s"%('getAllStates',str(len(states_list))))
            return (1,states_list)
        except:
            self.UserLogger.exception('[%s] == Exception =='%('getAllStates'))
            return (-1,[])
        
    def getAllStatesForAContentTypeBYName(self,app_label_t,model_t):
        try:
            states_list = StateContentType.objects.filter(StateContentType__app_label=app_label_t,StateContentType__model= model_t)
            self.UserLogger.debug("[%s] length of contenttypes_list is %s"%('getAllStatesForAContentTypeBYName',str(len(states_list))))
            return (1,states_list)
        except:
            self.UserLogger.exception('[%s] == Exception == applabel = %s, model = %s'%('getAllStates',app_label_t,model_t))
            return (-1,[])