from ThoughtXplore.txDatabaseHelper import DBhelper
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

UserLogger = logging.getLogger(LOGGER_USER)

def DBUpdateMenu(details):
    try:
        query = "SELECT * FROM txMenu_menu_edit(" + str(details['mid']) + ",'" + details['name'] + "','" + details['desc'] + "','" + details['murl'] + "'," + str(details['pid']) + ",'" + details['micon'] + "','" + details['maction'] + "','" + details['logsdesc'] + "','" + details['prev'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBUpdateMenu',query))
        result = DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBUpdateMenu',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdateMenu',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}


def DBUpdateMultiple(details):
    try:
        query = "SELECT * FROM txMenu_menu_statechange('" + details['csv_mid'] + "'," + str(details['mpid']) + ",'" + details['permission'] + "','" + details['logsdesc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBUpdateMultiple',query))
        result = DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBUpdateMultiple',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBUpdateMultiple',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}


def DBInertMenu(details):
    try:
        query = "SELECT * FROM txMenu_menu_insert('" + details['name'] + "','" + details['desc'] + "','" + details['murl'] + "'," + str(details['pid']) + ",'" + details['micon'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"    
        UserLogger.debug('[%s] %s'%('DBInertMenu',query))
        result = DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBInertMenu',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInertMenu',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
def DBAddMenuToGroup(details):
    try:
        query=  "SELECT * FROM txUser_groupmenu_insert(" + str(details['groupid']) + ",'" + details['menulist'] + "'," + str(details['menuid_len']) + ",'" + details['logsdesc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBAddMenuToGroup',query))
        result = DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBAddMenuToGroup',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBAddMenuToGroup',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}