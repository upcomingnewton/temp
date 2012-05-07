'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime
from ThoughtXplore.CONFIG import LOGGER_MISC
import logging

MiscLogger = logging.getLogger(LOGGER_MISC)

# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertState(details):
    try:
        #query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        query = "SELECT * FROM Security_StateInsert('" + details['name'] + "','" + details['desc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        MiscLogger.debug('[%s] %s'%('DBInsertState',query))
        result =  DBhelper.CallFunction(query)
        MiscLogger.debug('[%s] %s'%('DBInsertState',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertState',query)
        MiscLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBInsertPermission(details):
    try:
        #query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        query = "SELECT * FROM Security_PermissionInsert('" + details['name'] + "','" + details['desc'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        MiscLogger.debug('[%s] %s'%('DBInsertPermission',query))
        result =  DBhelper.CallFunction(query)
        MiscLogger.debug('[%s] %s'%('DBInsertPermission',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertPermission',query)
        MiscLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}