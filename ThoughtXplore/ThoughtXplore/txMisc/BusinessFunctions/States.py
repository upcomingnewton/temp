from ThoughtXplore.txMisc.models import  MiscState ,StateContentType
from ThoughtXplore.CONFIG import LOGGER_MISC
from ThoughtXplore.txMisc.DBFunctions.DatabaseFunctions import DBInsertState
from ThoughtXplore.txMisc.DBFunctions.DBMessages import decode
import logging

class StatesClass():
    def __init__(self):
        self.MiscLogger = logging.getLogger(LOGGER_MISC)

     #CRUD FUNCTIONS
        
    def CreateState(self,name,desc,by,ip):
            try:
                self.MiscLogger.debug('inside CreateState')
                details = {
                           'ip':ip,
                           'by':by,
                           'name':name,
                           'desc':desc,
                           }
                result = DBInsertState(details)
                self.MiscLogger.debug('[%s] %s,%s'%('CreateState',str(details),str(result)))
                return (result,decode(int(result['result']), result['rescode']))
            except:
                exception_log = ('[%s] %s,%s,%s,%s')%('CreateState',name,desc,by,ip)
                self.MiscLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while creating group')


    def getAllStates(self):
        try:
            states_list = MiscState.objects.all()
            self.MiscLogger.debug("[%s] length of stateslist is %s"%('getAllStates',str(len(states_list))))
            return (1,states_list)
        except:
            self.MiscLogger.exception('[%s] == Exception =='%('getAllStates'))
            return (-1,[])
    
    def getAllStatesForAContentTypeBYID(self,cid):
        try:
            states_list = MiscState.objects.filter(statecontenttype__StateContentType__id=cid)
            self.MiscLogger.debug("[%s] length of states list is %s"%('getAllStatesForAContentTypeBYID',str(len(states_list))))
            return (1,states_list)
        except:
            self.MiscLogger.exception('[%s] == Exception == cid = %s'%('getAllStatesForAContentTypeBYID',cid))
            return (-1,[])
        
    
    def getAllStatesForAContentTypeBYName(self,app_label_t,model_t):
        try:
            states_list = StateContentType.objects.filter(StateContentType__app_label=app_label_t,StateContentType__model= model_t)
            self.MiscLogger.debug("[%s] length of states list is %s"%('getAllStatesForAContentTypeBYName',str(len(states_list))))
            return (1,states_list)
        except:
            self.MiscLogger.exception('[%s] == Exception == applabel = %s, model = %s'%('getAllStates',app_label_t,model_t))
            return (-1,[])