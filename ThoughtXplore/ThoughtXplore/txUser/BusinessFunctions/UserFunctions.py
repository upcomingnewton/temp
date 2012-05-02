from django.db import models
from ThoughtXplore.txUser.models import User,Group,SecGroup_Comm
from ThoughtXplore.txMisc.enc_dec import Encrypt
from ThoughtXplore.txUser.DBFunctions.DatabaseFunctions import *
from ThoughtXplore.txUser.DBFunctions.DBMessages import db_messages,decode
from ThoughtXplore.txMenu.BusinessFunctions.LoginMenuFunctions import MakeGroupMenu
from cPickle import dumps, loads
from ThoughtXplore.CONFIG import LOGGER_USER
import logging
from ThoughtXplore.txMisc.Email import sendMail



class UserFnx(models.Model):
    
    def __init__(self):
        self.encrypt = Encrypt()
        self.UserLogger = logging.getLogger(LOGGER_USER)
        
    def AuthenticateUserFromSite(self,emailid,ip):
        try:
            to_emailid = self.encrypt.decrypt(emailid)
            s = to_emailid.split('___')
            details = {
                       'userid':int(s[0]),
                       'by':1,
                       'request_group':'authenticated_users',
                       'request_permission':'USER_AU',
                       'ip':ip,
                       'logsdesc':'UserAuthentication',
                       }
            result = DB_ChangeStateOfASingleUser(details)
            return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s,%s')%('AuthenticateUserFromSite',ip,emailid)
            self.UserLogger.exception(exception_log)
        
    def InsertUserFromSite(self,email,password,fname,mname,lname,gender,bday,entity,ip):
        try:
            user = {'email':email, 
                    'pass':self.encrypt.encrypt(password),
                    'fname':fname,
                    'lname':lname,
                    'mname':mname,
                    'gender':gender,
                    'bday':str(bday),
                    'entity':'system',
                    'state':'INSERT',
                    'group':'created_users',
                    'logsdesc':'INSERT;created_users',
                    'by_email':2,
                    'ip':ip}
            result = DBInsertUser(user)
            return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s,%s')%('InsertUserFromSite',ip,email)
            self.UserLogger.exception(exception_log)
    
    def LoginUser(self,email,password,_type,ip):
        try:
            details = {'email':email,
                           'pass':self.encrypt.encrypt(password),
                           'login_type':_type,
                           'ip':ip}
                            
            result = DBLoginUser(details)
            if( int(result['result']) >= 1):
                #MakeGroupMenu(result['groupid'])
                return(result, decode(int(result['result']),result['rescode']))
            else:
                return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s,%s')%('LoginUser',ip,email)
            self.UserLogger.exception(exception_log)
        
        
    def LogoutUser(self,loginid,out_from):
        try:

            details = {'loginid':self.encrypt.decrypt(loginid),
                       'logout_from':out_from,
                      }
            result = DBLogoutUser(details)
            return(result, decode(int(result['result']),result['rescode']))
        except:
            exception_log = ('[%s] %s')%('LogoutUser',loginid)
            self.UserLogger.exception(exception_log)
        
    def send_mail_test(self,email,userid,fname,ip):
        token= self.encrypt.encrypt(str(userid) + '___' + email)
        import time
        refs = int(time.time())
        token="http://labs-nitin.thoughtxplore.com/user/authenticate/email/"+token+"/" + str(refs) + "/"
        sendMail([ "upcomingnewton@gmail.com"],"no-reply@thoughtxplore.com","authenticate",token)
    
    
