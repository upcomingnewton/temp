from ThoughtXplore.txMisc.models import  MiscState ,StateContentType
from ThoughtXplore.CONFIG import LOGGER_MISC
import logging

class StatesClass():
    def __init__(self):
        self.MiscLogger = logging.getLogger(LOGGER_MISC)

    def getAllStates(self):
        try:
            states_list = MiscState.objects.all()
            self.MiscLogger.debug("[%s] length of stateslist is %s"%('getAllStates',str(len(states_list))))
            return (1,states_list)
        except:
            self.MiscLogger.exception('[%s] == Exception =='%('getAllStates'))
            return (-1,[])
        
    def getAllStatesForAContentTypeBYName(self,app_label_t,model_t):
        try:
            states_list = StateContentType.objects.filter(StateContentType__app_label=app_label_t,StateContentType__model= model_t)
            self.MiscLogger.debug("[%s] length of states list is %s"%('getAllStatesForAContentTypeBYName',str(len(states_list))))
            return (1,states_list)
        except:
            self.MiscLogger.exception('[%s] == Exception == applabel = %s, model = %s'%('getAllStates',app_label_t,model_t))
            return (-1,[])