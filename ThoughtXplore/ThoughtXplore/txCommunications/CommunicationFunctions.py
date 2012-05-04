from ThoughtXplore.txUser.models import User, UserGroup, Group



from ThoughtXplore.txCommunications.models import Communication_Templates, Communication_Type,Communication_Groups
from cPickle import dumps, loads
import string
from ThoughtXplore.txMisc.Encryption.enc_dec import Encrypt
from django.core import mail
#from mailer import send_mail
from ThoughtXplore.txMisc.Misc.Email import sendMail
from ThoughtXplore.txCommunications.DatabaseFunctions import DBInsertComm, DBInsertCommTemplate
from datetime import datetime
from django.http import HttpRequest,HttpResponse
from ThoughtXplore.txMisc.Misc.MiscFunctions import split
from ThoughtXplore import CONFIG
from ThoughtXplore.txUser.BusinessFunctions.UserFunctions import UserFnx
import time


def send_validation_email(email,userid,fname,ip):
   
    temp=Communication_Templates.objects.filter(TemplateName="Email_Validation")  
    Subject="Account Creation"
    ##add user function
    #send email
    for e in temp:
        Template=loads(e.TemplateFormat.decode("base64").decode("zip"))
        reqparam=loads(e.paramList.decode("base64").decode("zip"))
    encdec=Encrypt()
    token=encdec.encrypt(str(userid) + '___' + email)
    refs = int(time.time())
    token="http://uiet.thoughtxplore.com/user/authenticate/email/"+token+"/" + str(refs) + "/"
    #token="http://uiet.thoughtexplore.com/user/authenticate/email/"+token+"/"
    
    param_list_=[fname]    
    
    reqparam_=string.split(reqparam,',')
    
    param_list_.append(str(token))
    for i,v in zip(reqparam_,param_list_):    
        Template=Template.replace(i, v)
    message=Template
    '''
    not needed -sarvpriye
    # here is what you need to do 
    # 1. add an entry to communication type of "email"
    # 2. add an entry to communication for all this template and all
    '''
    #to get group id of group named as "Group_Comm_EmailValidation"
    group=Group.objects.filter(GroupName="Group_Comm_EmailValidation")
    userlist=str(userid)+","
    
    for i in group:
        group_id=i.id
    userfnx=UserFnx()
    print "user list"
    print userlist
    
    print "till here too"
    #try:
        
        #mail.send_mail(Subject, message,"AuthenticateUserDaemon@tx.com", [email,"sarvpriye98@gmail.com", "upcomingnewton@gmail.com"], fail_silently=True)
    #except:
    sendMail([email,"sarvpriye98@gmail.com", "upcomingnewton@gmail.com"],"no-reply@thoughtxplore.com",Subject,message)
    print message 
    
    result= userfnx.AddUserToSecGroupForComm(group_id, userlist, 1, ip)
    #print result
    return result


def send_notice(details):
    
    print "here"
    
    ip= details['ip']
    #toGroupID=0 means to all groups
    '''
    if "details"  in  HttpRequest.sessions.keys():
        session_data=HttpRequest.session['details']
        fromUserID= session_data["userid"]
    else:
        return HttpResponse("UNAUTHORIZED ACCESS")
    '''
    
    fromUserID=details["fromUserID"]
    for i in UserGroup.objects.filter(User=fromUserID):
        print i.id
        print "lol"
        print i.Group_id
        print "lol"
        if not(i.Group_id==3):
            return HttpResponse("UNAUTHORIZED ACCESS")
        
    print details
    print "till here"
    for i in Communication_Type.objects.filter(type="notice"):
        CommTypeID=i.id
    
    if not Communication_Templates.objects.filter(TemplateName="Default").exists():
        paramList_=  dumps(" ").encode("zip").encode("base64").strip()
        TemplateFormat_=dumps(" ").encode("zip").encode("base64").strip()
    
        detail={
                     'CommType':CommTypeID,
                     'TemplateName':'Default',
                     'paramList':paramList_,
                     'TemplateFormat': TemplateFormat_,
                     'Author':fromUserID,
                     'ip':ip,
                     }
        DBInsertCommTemplate(detail)
    print "here 1"
    for i in Communication_Templates.objects.filter(TemplateName="Default"):
        TemplateID=i.id  
        
    subject= details["subject"]
    #togroupIDs= details("ToGroupIDs_")
    paramList= ""
    '''
    if(togroupIDs!=""):
        a=split(togroupIDs)
        togroupIDs_=[int(i) for i in a]
    '''    
    to_group_list="0"
    '''
    for i in togroupIDs_:
        to_group_list+=str(i)+","
    '''
    paramList=dumps(paramList).encode("zip").encode("base64").strip()
    message=dumps(details['message']).encode("zip").encode("base64").strip()
    subject=dumps(subject).encode("zip").encode("base64").strip()


    
    param = {
           'FromUserID':fromUserID,
           'Subject':subject,
           'CommTypeID':str(CommTypeID),
           'TemplateID':str(TemplateID),
           'ParameterDict':paramList,
           'ToGroupIDs':to_group_list,
           'ip':ip,
           'comm_code_name': 'General Notice',
           'Message':message,
           'TimeStamp':datetime.now(),

            }
    print param
    
    
    
    result=DBInsertComm(param)
    
    return result


def addtemplate(HttpRequest):
    authorID= int(HttpRequest.POST["authorID"])
    CommType=Communication_Type.objects.filter(type="email")
    for i in CommType:
        CommTypeID=i.id
    print CommTypeID
    TemplateName= HttpRequest.POST["TemplateName"]
    paramList= HttpRequest.POST["paramList"]
    TemplateFormat= HttpRequest.POST["TemplateFormat"]
    paramList_=  dumps(paramList).encode("zip").encode("base64").strip()
    TemplateFormat_=dumps(TemplateFormat).encode("zip").encode("base64").strip()
    template= Communication_Templates()
    ip=HttpRequest.META['REMOTE_ADDR']
    print "test"
    details={
             'CommType':CommTypeID,
             'TemplateName':TemplateName,
             'paramList':paramList_,
             'TemplateFormat':TemplateFormat_,
             'Author':authorID,
             'ip':HttpRequest.META['REMOTE_ADDR'],
             }
    DBInsertCommTemplate(details)
    
    return HttpResponse("Done")



def send_mails(param):
    return 1
#def send_mails(param):
#    
#    email_code_name=param['comm_code_name']
#    print param
#    to_id_list=[]
#    if(email_code_name=='Auth_Email'):
#        for a in param['touserIDs']:   
#                to_id_list.append(a)
#
#    for a in param['togroupIDs']:
#            for b in UserGroup.objects.filter(Group=a):
#                to_id_list.append(b.User_id)
#       
#    to_email_list=[]
#    for e in to_id_list:
#        for f in User.objects.filter(id=e):
#            to_email_list.append(f.UserEmail)
#    
#    for e in User.objects.filter(id=param['fromUserID']):
#        from_=e.UserEmail
#    
#    for e in Communication_Templates.objects.filter(id=param['TemplateID']):
#        Template=loads(e.TemplateFormat.decode("base64").decode("zip"))
#        reqparam=loads(e.paramList.decode("base64").decode("zip"))
#    paramList=param['paramList']
#    param_list_=[]
#   
#    param_list_=string.split(paramList,',')
#    
#    
#    reqparam_=string.split(reqparam,',')
#    
#        
#    Template=str(Template)
#    if(email_code_name=='Auth_Email'):
#        encdec=Encrypt()
#        for i in to_email_list:
#            token=encdec.encrypt(i)
#            token="http://127.0.0.1:8000/user/authenticate/email/"+token+"/"
#            print token
#        param_list_.append(str(token))
#    for i,v in zip(reqparam_,param_list_):    
#        Template=Template.replace(i, v)
#    message=Template
#    print "till here too"
#    datatuple=[param['Subject'], message,from_,to_email_list]
#   
#    #auth_user_="auth_user"
#    #auth_password_="auth_password"
#    to_email_list.append("sarvpriye98@gmail.com")
#    send_mail(param['Subject'], message,from_, to_email_list, fail_silently=True)
#    timestamp=datetime.now()
#
#    #send_mass_mail(datatuple, fail_silently=True)    
#    #db entry
#    to_id_list_=""
#    to_group_list=""
#    
#    to_email_list_=""
#    print param['togroupIDs']
#    for a in to_email_list:
#        to_email_list_+= a+", "
#    if(param['togroupIDs']!=""):
#        for a in param['togroupIDs']:
#            to_group_list+=""+str(a)+","
#    for a in to_id_list:
#        if(to_id_list_==""): to_id_list_=str(a)
#        else:
#            to_id_list_=","+str(a)
#    if(to_id_list_==""):
#        to_id_list_="Null"
#    
#    print "till here"
#    paramList=dumps(paramList).encode("zip").encode("base64").strip()
#    
#    sent_message={
#                       'FromUserID': param['fromUserID'],
#                       'CommTypeID':str(param['CommTypeID']),
#                       'TemplateID': str(param['TemplateID']),
#                       'Subject':param['Subject'],
#                       'ParameterDict': paramList,
#                       'ToGroupIDs':to_group_list,
#                       'Message':message,
#                       'TimeStamp':timestamp,
#                       'ip':param['ip']
#                               } 
#    print sent_message
#    print "sm"
#    DBInsertComm(sent_message)
#    return 1