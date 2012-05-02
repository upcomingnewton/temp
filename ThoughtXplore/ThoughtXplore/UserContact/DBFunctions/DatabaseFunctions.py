'''
Created on Mar 3, 2012

@author: nitin
'''
from ThoughtXplore.txDatabaseHelper import DBhelper
from datetime import datetime
from ThoughtXplore.CONFIG import LOGGER_USER
import logging

UserLogger = logging.getLogger(LOGGER_USER)

# USER CONTACT INFO SYSTEM
### ========================================================================================================  ### 


def DBContactInfoInsert(details):
    try:
        query = "SELECT * FROM contactinfo_insert(" + str(details['uid']) + ",'" + details['req_per'] + "','" + details['Mobileno'] + "','" + details['Phoneno'] + "','" + details['AltEmailAdress'] + "','" + details['FatherName'] + "','" + details['FatherContactNo'] + "','" + details['MotherName'] + "','" + details['MotherContactNo'] + "','" + details['AlternateAdress'] + "','" + details['Adress'] + "'," +str(details['by_user']) + ",'" + details['ip'] + "');"
        #""# "SELECT * FROM txUser_user_insert('" + userdetails['email'] + "','" + userdetails['pass'] + "','" + userdetails['fname'] + "','" + userdetails['mname'] + "','" + userdetails['lname'] + "','" + userdetails['gender'] + "','" + userdetails['bday'] + "','" + userdetails['entity'] + "','" + userdetails['state'] + "','" + userdetails['group'] + "','" + userdetails['logsdesc'] + "','" + str(userdetails['by_email']) + "','" + userdetails['ip'] +"'); "
        UserLogger.debug('[%s] %s'%('DBContactInfoInsert',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBContactInfoInsert',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBContactInfoInsert',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
        
def DBContactInfoUpdate(details):
    try:
        query = "SELECT * FROM contactinfo_insert(" + str(details['uid']) + ",'" + details['req_per'] + "','" + details['Mobileno'] + "','" + details['Phoneno'] + "','" + details['AltEmailAdress'] + "','" + details['FatherName'] + "','" + details['FatherContactNo'] + "','" + details['MotherName'] + "','" + details['MotherContactNo'] + "','" + details['AlternateAdress'] + "','" + details['Adress'] + "'," +str(details['by_user']) + ",'" + details['ip'] + "','" + details['logsdec'] + "');"
        #query =""# "SELECT * FROM user_login('" + logindetails['email'] + "','" + logindetails['pass'] + "'," + str(logindetails['login_type']) + ",'" + logindetails['ip'] + "','" + str(datetime.now()) + "');"
        UserLogger.debug('[%s] %s'%('DBContactInfoUpdate',query))
        result =  DBhelper.CallFunction(query)
        UserLogger.debug('[%s] %s'%('DBContactInfoUpdate',result))
        return result[0]
    except:
        exception_log = "[%s] %s"%('DBContactInfoUpdate',query)
        UserLogger.exception(exception_log)
        return {'result':-1,'rescode':-1}
    
