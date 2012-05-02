
#from ThoughtXplore.txMisc.enc_dec import Encrypt 
from ThoughtXplore.txMenu.models import Menu , GroupMenu
from ThoughtXplore.txMenu.BusinessFunctions.MenuFunctions import MenuFnx 
from ThoughtXplore.txMenu.DBFunctions.DatabaseFunctions import DBAddMenuToGroup
from ThoughtXplore.txMenu.DBFunctions.DBMessages import decode
from ThoughtXplore.txLogging import MenuLogger
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

class ModifiedMenu():
    MenuName = "None"
    MenuDesc = "None"
    MenuUrl = "None"
    MenuPid = "None"
    SCI = "None"
    MenuIcon = "None"
    Selected = "false"


class GroupMenuFunctions():
    def __init__(self):
        Menuobj = Menu()
        GroupMenuObj = GroupMenu()
        self.UserLogger = logging.getLogger(LOGGER_USER)
    # SELECT FUNCTIONS
    
    def GetAllMenuObjectsByGroupid(self,gid):
        try:
            groupmenulist =  Menu.objects.filter(groupmenu__Group__id=gid,groupmenu__Active=1)
            self.UserLogger.debug('[%s] gid=%s, %s'%('GetAllMenuObjectsByGroupid',gid,str(groupmenulist)))
            return (1,groupmenulist)
        except:
            exception_log = ('[%s] gid = %s')%('GetAllMenuObjectsByGroupid', gid)
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
    def getMenuIDbyGroupIdForGroup(self,gid):
        try:
            groupmenulist = GroupMenu.objects.filter(Group__id=gid)
            self.UserLogger.debug('[%s] gid=%s, %s'%('GetAllMenuObjectsByGroupid',gid,str(groupmenulist)))
            return (1,groupmenulist)
        except:
            exception_log = ('[%s] gid = %s')%('GetAllMenuObjectsByGroupid', gid)
            self.UserLogger.exception(exception_log)
            return (-1,[])
        
    # DATA BASE FUNCTIONS

    def CreateGroupMenu(self,gid,mlist,by,ip):
        try:
                self.UserLogger.debug('[%s] mlist= %s'%('CreateGroupMenu',mlist))
                str_selected_menu = ''
                count  = 0
                for x in mlist:
                    str_selected_menu = str_selected_menu + x + ','
                    count = count + 1
                str_selected_menu = str_selected_menu[:-1]
                self.UserLogger.debug('[%s] str_selected_menu= %s'%('CreateGroupMenu',str_selected_menu))
                details = {
                           'groupid':gid,
                           'menulist':str_selected_menu,
                           'menuid_len':count,
                           'logsdesc':'logsdesc',
                           'by':by,
                           'ip':ip,
                           }
                res2 = DBAddMenuToGroup(details)
                self.UserLogger.debug('[%s] %s,%s'%('CreateGroupMenu',str(details),str(res2)))
                return (res2,decode(int(res2['result']), res2['rescode']))
        except:
            exception_log = ('[%s] %s %s,%s,%s')%('CreateGroupMenu',gid,mlist,by,ip)
            self.UserLogger.exception(exception_log)
            return (-1,'Exception Occoured at Business Functions of CreateGroupMenu')
        
    # HELPER FUNCTIONS
    
    ## gets a list of all menu's and menu id's selected in a particular
    # group and arranges them to be sent to a view, along with a chceked 
    # functionality 

    
    def SetGroupMenuForEditing(self,menulist,groupmenulist):
        final_result = []
        temp = []
        menu_fnx_obj = MenuFnx()
        SortedMenuList = menu_fnx_obj.SortMenuByParent(menulist)
        if( SortedMenuList[0] == 1):
            SortedMenuList = SortedMenuList[1]
            for menulist in SortedMenuList:
                temp = []
                for menu in menulist:
                    ret_val = self.CheckForPresenece(menu,groupmenulist)
                    if ret_val is True:
                        temp.append(self.makeModifiedMenuObj(menu,"true"))
                    else:
                        temp.append(self.makeModifiedMenuObj(menu,"false"))
                final_result.append(temp)
            
        return final_result
    
    def CheckForPresenece(self,menuobj, groupmenulist):
            for x in groupmenulist:
                if menuobj.id == x.id:
                    return True
            return False

    def makeModifiedMenuObj(self,menuobj,checked):
        myobj = ModifiedMenu()
        myobj.MenuName = menuobj.MenuName
        myobj.MenuDesc = menuobj.MenuDesc
        myobj.MenuIcon = menuobj.MenuIcon
        myobj.MenuPid = menuobj.MenuPid
        myobj.MenuUrl = menuobj.MenuUrl
        myobj.SCI = menuobj.SCI.id
        myobj.Selected = checked
        myobj.id = menuobj.id
        return myobj
