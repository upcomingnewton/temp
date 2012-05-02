from ThoughtXplore.txMenu.models import Menu, GroupMenu
from ThoughtXplore.txMenu.DBFunctions.DatabaseFunctions import DBInertMenu,DBUpdateMenu,DBUpdateMultiple
from ThoughtXplore.txMenu.DBFunctions.DBMessages import decode
from django.db import models
from cPickle import dumps, loads
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

class MenuFnx(models.Model):
    
    def __init__(self):
        self.UserLogger = logging.getLogger(LOGGER_USER)
    
    # select functions
    def getParentMenus(self):
        try:
            menulist =  Menu.objects.filter(MenuPid__exact=-1)
            self.UserLogger.debug('[%s] %s'%('getParentMenus',str(menulist)))
            return (1,menulist)
        except:
            exception_log = ('[%s]')%('getParentMenus')
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
    def getMenuIDbyGroupID(self,gid):
        try:
            menulist = GroupMenu.objects.filter(Group__exact=gid)
            self.UserLogger.debug('[%s] %s'%('getParentMenus',str(menulist)))
            return (1,menulist)
        except:
            exception_log = ('[%s]')%('getMenuIDbyGroupID')
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
    def getSingleMenuItemById(self,menuid):
        try:
            menulist =  Menu.objects.filter(id__exact=menuid)
            self.UserLogger.debug('[%s] %s'%('getParentMenus',str(menulist)))
            return (1,menulist)
        except:
            exception_log = ('[%s]')%('getSingleMenuItemById')
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
    def getAllMenu(self):
        try:
            menulist =  Menu.objects.all()
            self.UserLogger.debug('[%s] %s'%('getParentMenus',str(menulist)))
            return (1,menulist)
        except:
            exception_log = ('[%s]')%('getAllMenu')
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
        
    # CRUD FUNCTIONS
    def CreateMenuFromSite(self,name,desc,murl,pid,micon,by,ip):  
        self.UserLogger.debug('inside CreateMenuFromSite')
        try: 
            details = {'name':name,
                       'desc':desc,
                       'murl':murl,
                       'pid':pid,
                       'micon':micon,
                       'by':by,
                       'ip':ip,
                       }
            result = DBInertMenu(details)
            self.UserLogger.debug('[%s] %s,%s'%('UpdateMultipleMenuFromSite',str(details),str(result)))
            return (result,decode(int(result['result']), result['rescode']))
        except:
            exception_log = ('[%s] %s,%s,%s,%s,%s,%s,%s')%('CreateMenuFromSite',name,desc,murl,pid,micon,by,ip)
            self.UserLogger.exception(exception_log)
            return (-1,'Exception Occoured at Business Functions while creating menu')
    
    def UpdateMenuFromSite(self,mid,name,desc,murl,pid,micon,by,ip):
        try:
            tempm = Menu.objects.get(id=mid)
            #TODO : yoy need to dump the previous menu's load here
            details = {'mid':mid,
                       'name':name,
                       'desc':desc,
                       'murl':murl,
                       'pid':pid,
                       'micon':micon,
                       'maction':'UPDATE',
                       'logsdesc': tempm.encode("zip").encode("base64").strip(),
                       'prev':'prev',
                       'by':by,
                       'ip':ip,
                       }
            result = DBUpdateMenu(details)
            self.UserLogger.debug('[%s] %s,%s'%('UpdateMultipleMenuFromSite',str(details),str(result)))
            return (result,decode(int(result['result']), result['rescode']))
        except:
            exception_log = ('[%s] %s %s,%s,%s,%s,%s,%s,%s')%('UpdateMenuFromSite',mid,name,desc,murl,pid,micon,by,ip)
            self.UserLogger.exception(exception_log)
            return (-1,'Exception Occoured at Business Functions while updating menu')

    def UpdateMultipleMenuFromSite(self,csv_mid,permission,mpid,by,ip):
        try:
            details = {'csv_mid':csv_mid,
                       'mpid':mpid,
                       'permission':permission,
                       'logsdesc':csv_mid + '-' + permission,
                       'by':by,
                       'ip':ip,
                       }
            result = DBUpdateMultiple(details)
            self.UserLogger.debug('[%s] %s,%s'%('UpdateMultipleMenuFromSite',str(details),str(result)))
            return (result,decode(int(result['result']), result['rescode']))
        except:
            exception_log = ('[%s] %s %s,%s,%s,%s')%('UpdateMultipleMenuFromSite',str(csv_mid),str(permission),str(mpid),str(by),str(ip))
            self.UserLogger.exception(exception_log)
            return (-1,'Exception Occoured at Business Functions while updating multiple menu')
    
    
    
    #### HELPER FUNCTIONS
    

    
    def SortMenuByParent(self,menulist):
        try:
            final_result = []
            temp = []
            for menu in menulist:
                temp = []
                if menu.MenuPid == -1:
                        temp.append(menu)
                        for x in menulist:
                                if x.MenuPid == menu.id:
                                        temp.append(x)
                final_result.append(temp)
            self.UserLogger.debug('[%s] menulist = %s  final_result = %s'%('SortMenuByParent',str(menulist),str(final_result)))
            return (1,final_result)
        except:
            exception_log = ('[%s] %s ')%('SortMenuByParent',str(menulist))
            self.UserLogger.exception(exception_log)
            return (-1,[])