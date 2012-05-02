'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

UserLogger = logging.getLogger(LOGGER_USER)

# USER SYSTEM
### ========================================================================================================  ### 


def DBInsertUser(userdetails):
    try:
        query = "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        UserLogger.debug('[%s] %s'%('DBInsertUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBInsertUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBInsertUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBLoginUser(logindetails):
    try:
        query = "SELECT * FROM user_login('" + logindetails['email'] + "','" + logindetails['pass'] + "'," + str(logindetails['login_type']) + ",'" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
        UserLogger.debug('[%s] %s'%('DBLoginUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBLoginUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBLoginUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
def DBLogoutUser(details):
    try:
        query = "SELECT * FROM user_logout(" + str(details['loginid']) + "," +  str(details['logout_from']) + ",'" + str(datetime.now()) + "');"
        UserLogger.debug('[%s] %s'%('DBLogoutUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBLogoutUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBLogoutUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
def DBAuthenicateUser(auth_details):
    try:
        #"SELECT * FROM txUser_user_statechange('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['state'] + "','" + auth_details['perm'] + "','" + auth_details['ip'] + "','" + auth_details['logsdesc'] + "');"
        query = "SELECT * FROM txUser_user_statechange('" + auth_details['to_email'] + "','" + auth_details['by_email'] + "','" + auth_details['state'] + "','" + auth_details['perm'] + "','" + auth_details['ip'] + "','" + auth_details['logsdesc'] + "');"
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBAuthenicateUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DB_ChangeStateOfASingleUser(details):
    try:
        query = "SELECT * FROM txUser_user_statechange_single(" + str(details['userid']) + "," + str(details['by']) + ",'" + details['request_group'] + "','" + details['request_permission'] + "','" + details['ip'] + "','" + details['logsdesc'] + "');"
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBAuthenicateUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
### ========================================================================================================  ###        
        
# GROUP FUNCTIONS

def DBCreateGroup(details):
    try:
        query=  "SELECT * FROM txUser_group_insert('" + details['groupname']  + "','" + details['groupdesc'] + "'," + str(details['group_type_id']) + ",'" + details['entity']  + "','" + details['request'] + "'," + str(details['by']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBAuthenicateUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}

### ========================================================================================================  ###  

# USER GROUP FUNCTIONS

def DBAddUserToGroup(details):
    try:
        query =  "SELECT * FROM txUser_usergroup_insert("  + str(details['groupid']) + ",'" + details['userid'] + "','" + details['logsdesc'] + "'," + str(details['by_user']) + ",'" + details['ip'] + "');"
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBAuthenicateUser',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBAuthenicateUser',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
### ========================================================================================================  ###  

def DBCreateSecGroupForCommunications(details):
    query = "SELECT * FROM  SecGroup_Comm_insert('" + details['groupid'] + "','" + details['permission'] + "','" + details['params'] + "','[-1]','" + details['logdesc'] + "'," + details['by'] + ",'" + details['ip'] + "');"
    print query
    #result =  DBhelper.CallFunction(query)
    #return result





def DBAddUsertoSecGroupForCommunications(details):
    query= "SELECT * FROM SecGroup_Comm_appned(" + str(details['groupid']) + ",'" + details['userid'] + "','" + details['params'] + "','" + details['permission'] + "','" + str(details['by']) + "');"
    print query
    result =  DBhelper.CallFunction(query)
    return result[0]

