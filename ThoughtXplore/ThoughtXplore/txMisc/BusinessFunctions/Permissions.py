from ThoughtXplore.txMisc.models import  MiscPermission ,PermissionContentType
from ThoughtXplore.CONFIG import LOGGER_MISC
from ThoughtXplore.txMisc.DBFunctions.DatabaseFunctions import DBInsertPermission
from ThoughtXplore.txMisc.DBFunctions.DBMessages import decode
import logging



class PermissionsClass():
    def __init__(self):
        self.MiscLogger = logging.getLogger(LOGGER_MISC)

     #CRUD FUNCTIONS
        
    def CreatePermission(self,name,desc,by,ip):
            try:
                self.MiscLogger.debug('inside CreatePermission')
                details = {
                           'ip':ip,
                           'by':by,
                           'name':name,
                           'desc':desc,
                           }
                result = DBInsertPermission(details)
                self.MiscLogger.debug('[%s] %s,%s'%('CreatePermission',str(details),str(result)))
                return (result,decode(int(result['result']), result['rescode']))
            except:
                exception_log = ('[%s] %s,%s,%s,%s')%('CreatePermission',name,desc,by,ip)
                self.MiscLogger.exception(exception_log)
                return (-1,'Exception Occoured at Business Functions while CreatePermission')


    def getAllPermissions(self):
        try:
            perm_list = MiscPermission.objects.all()
            self.MiscLogger.debug("[%s] length of perm_list is %s"%('getAllPermissions',str(len(perm_list))))
            return (1,perm_list)
        except:
            self.MiscLogger.exception('[%s] == Exception =='%('getAllPermissions'))
            return (-1,[])
        
    def getAllPermissionsForAContentTypeByID(self,cid):
        try:
            perm_list = MiscPermission.objects.filter(permissioncontenttype__PermissionContentType__id=cid)
            self.MiscLogger.debug("[%s] length of perm_list is %s"%('getAllPermissionsForAContentTypeByID',str(len(perm_list))))
            return (1,perm_list)
        except:
            self.MiscLogger.exception('[%s] == Exception ==, cid = %s'%('getAllPermissionsForAContentTypeByID',cid))
            return (-1,[])
