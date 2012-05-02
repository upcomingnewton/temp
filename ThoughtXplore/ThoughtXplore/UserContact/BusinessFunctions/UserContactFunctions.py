from ThoughtXplore.CONFIG import LOGGER_USER
from ThoughtXplore.UserContact.DBFunctions.DatabaseFunctions import DBContactInfoInsert, DBContactInfoUpdate
from ThoughtXplore.UserContact.DBFunctions.DBMessages import decode
from ThoughtXplore.UserContact.models import UserContact
from pickle import dumps
import logging

class UserContactFnx():
    def __init__(self):
        self.ContactLogger = logging.getLogger(LOGGER_USER)
        
    # CRUD FUNCTIONS
    def InsertContactDetails(self,uid,req_per,Mobileno,Phoneno,AltEmailAdress,FatherName,FatherContactNo,MotherName,MotherContactNo,AlternateAdress,Adress,by_user,ip):
        
        details = {     'uid':uid, 
                        'req_per':'INSERT',
                        'Mobileno':Mobileno,
                        'Phoneno':Phoneno,
                        'AltEmailAdress':AltEmailAdress,
                        'FatherName':FatherName,
                        'FatherContactNo':FatherContactNo,
                        'MotherName':MotherName,
                        'MotherContactNo':MotherContactNo,
                        'AlternateAdress':AlternateAdress,
                        'Adress':Adress,
                        'by_user':by_user,
                        'ip':ip,
                    }
        try:
                result = DBContactInfoInsert(details)
                return(result, decode(int(result['result']),result['rescode']))
        except:
                exception_log = ('[%s] details = %s')%('InsertContactDetails',str(details))
                self.UserLogger.exception(exception_log)
                return (-1,'Some exception has occured while inserting your contact details.Site administrators have been alerted. Please try after sometime')
                
    def UpdateContactDetails(self,uid,req_per,Mobileno,Phoneno,AltEmailAdress,FatherName,FatherContactNo,MotherName,MotherContactNo,AlternateAdress,Adress,by_user,ip):
        
        # get user object from database
        contactobj = self.getUserContactObjectByUserid(uid)
        logsdesc = ""
        if( contactobj[0] != 1 or contactobj[0] == -1 or contactobj[1] is None ):
            return (-1, 'Error getting previous values from the database. Please try after sometime.')
        else:
            try:
                logsdesc = dumps(contactobj).encode("zip").encode("base64")
            except:
                exception_log = ('[%s] exception in dumping logsdesc, details = %s')%('UpdateContactDetails',str(contactobj))
                self.UserLogger.exception(exception_log)
                return (-1,'Error. Error in dumping previous values to maintaince. Please try after sometiome.')
        # pickle the object and make logs description of it
        
        details = {     'uid':uid, 
                        'req_per':'INSERT',
                        'Mobileno':Mobileno,
                        'Phoneno':Phoneno,
                        'AltEmailAdress':AltEmailAdress,
                        'FatherName':FatherName,
                        'FatherContactNo':FatherContactNo,
                        'MotherName':MotherName,
                        'MotherContactNo':MotherContactNo,
                        'AlternateAdress':AlternateAdress,
                        'Adress':Adress,
                        'by_user':by_user,
                        'ip':ip,
                        'logsdesc':logsdesc,
                    }
        try:
                
                result = DBContactInfoUpdate(details)
                return(result, decode(int(result['result']),result['rescode']))
        except:
                exception_log = ('[%s] details = %s')%('UpdateContactDetails',str(details))
                self.UserLogger.exception(exception_log)
                return (-1,'Some exception has occured while updating your contact details.Site administrators have been alerted. Please try after sometime')
        
    #SELECT FUNCTIONS
    
    def getUserContactObjectByUserid(self,userid):
        try:
            details = UserContact.objects.filter(User=userid)
            self.UserLogger.debug('[%s] userid = %s, details  = %s'%('getUserContactObjectByUserid',userid,details))
            return (1,details)
        except:
            exception_log = ('[%s] userid = %s')%('getUserContactObjectByUserid',str(userid))
            self.UserLogger.exception(exception_log)
            return (-1,())
    