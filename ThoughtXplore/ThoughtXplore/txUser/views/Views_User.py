# Create your views here.
import sys
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
import datetime
import random
from django.core.urlresolvers import reverse
from ThoughtXplore.txUser.models import User
from ThoughtXplore.txUser.BusinessFunctions import UserFunctions
#from ThoughtXplore.txUser.views.Views_MiscFnx import CheckAndlogout
from ThoughtXplore.txMisc.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.enc_dec import Encrypt
from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from ThoughtXplore.txMisc import enc_dec
from ThoughtXplore.txLogging.UserLog import UserDebugLog
from ThoughtXplore.txLogging import ExceptionLog
from ThoughtXplore.CONFIG import LOGGER_USER, SESSION_MESSAGE
import logging
from django.views.decorators.cache import never_cache

LoggerUser = logging.getLogger(LOGGER_USER)


@never_cache
def Login_index(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
            mlist = CheckAndlogout(HttpRequest)
            msglist += mlist
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response("UserSystem/user/Login.html",{},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[Login_index][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')
    
    
@never_cache
def log_in(HttpRequest):
        msglist = []
        usrfn = UserFunctions.UserFnx()
        enc = Encrypt()
        ip = HttpRequest.META['REMOTE_ADDR']
        try:
            CheckAndlogout(HttpRequest)
            email = ''
            password = ''
            if 'LoginUser_email' in HttpRequest.POST.keys():
                email = HttpRequest.POST['LoginUser_email']
                email_val = EmailValidate(email)
                if( email_val.validate() != 1):
                    msglist.append('invalid email adress')
            else:
                msglist.append('email required')
            if 'LoginUser_pass' in HttpRequest.POST.keys():
                password = HttpRequest.POST['LoginUser_pass']
                if( len(password) < 1):
                    msglist.append('password required')
            else:
                msglist.append('password required')
            if len(msglist) > 0:
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/user/login/')
            else:
                res = usrfn.LoginUser(email, password,1, ip)
                result = res[0]
                if( result['result'] == 1):
                    token = {"userid":result['userid'],"groupid":result['groupid'],"loginid":enc.encrypt( str(result['loginid']))}
                    #print token
                    HttpRequest.session["details"] = token
                    #print 'i have reached here'
                    return HttpResponseRedirect('/user/dashboard/')
                else:
                    # handle other cases here like user is not active and all that
                    LoggerUser.error(res)
                    msglist.append(res[1])
                    HttpRequest.session[SESSION_MESSAGE] = msglist
                    return HttpResponseRedirect('/error/')
        except:
            LoggerUser.exception('[log_in][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
            
        
@never_cache
def log_out(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = []
    try:
        if "details" in HttpRequest.session.keys():
            token = HttpRequest.session['details']
            print token
            logout_user = UserFunctions.UserFnx()
            res =  logout_user.LogoutUser(token['loginid'],1)
            result = res[0]
            if( result['result'] == 1):
                del HttpRequest.session['details']
                return HttpResponseRedirect('/user/login/')
            else:
                LoggerUser.error(res)
                msglist.append(res[1])
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/error/')
        else:
            return HttpResponseRedirect('/user/login/')
    except:
            LoggerUser.exception('[log_out][%s] Exception '%(ip))
            msglist.append('Some Error has occoured')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    
@never_cache
def CreateUserFromSite(HttpRequest):
    #return HttpResponse(str(HttpRequest))
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = []
    try:
        email = HttpRequest.POST['RegisterUser_email']
        email_val = EmailValidate(email)
        if( email_val.validate() != 1):
            msglist.append('invalid email adress')
        pass1 = HttpRequest.POST['RegisterUser_pass']
        pass2 = HttpRequest.POST['RegisterUser_pass2']
        if( pass1 != pass2):
            msglist.append('passwords do not match')
        str_val = StringValidate()
        fname = HttpRequest.POST['RegisterUser_fname']
        if(str_val.validate_alphastring(fname) != 1):
                msglist.append('first name should contain only alphabets')
        mname = HttpRequest.POST['RegisterUser_mname']
        if( len(mname) > 0 ):
            if(str_val.validate_alphastring(mname) != 1):
                msglist.append('middle name should contain only alphabets')
        lname = HttpRequest.POST['RegisterUser_lname']
        if(str_val.validate_alphastring(lname) != 1):
                msglist.append('last name should contain only alphabets')
        bday = HttpRequest.POST['RegisterUser_dob']
        bday = bday.split('/')
        try:
            bday = datetime.date(int(bday[2]),int(bday[0]),int(bday[1]))
        except ValueError as err:
            msglist.append('Invalid Birthdate, '+ err.message)
        gender = HttpRequest.POST['RegisterUser_gender']
        if gender== "-1" :
            msglist.append('Please select your gender')
            
        if ( len(msglist) > 0 ):
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/register/')
        else:
            insfnx = UserFunctions.UserFnx()
            res = insfnx.InsertUserFromSite(email, pass2, fname, mname, lname, gender, bday,'system',HttpRequest.META['REMOTE_ADDR'])
            result = res[0]
            if( result['result'] >= 1 ):
                msglist.append('account created. an email has been sent in this regard.')
                HttpRequest.session[SESSION_MESSAGE] = msglist
                insfnx.send_mail_test(email, result['rescode'], fname, HttpRequest.META['REMOTE_ADDR'])
                encrypt = Encrypt()
                return HttpResponseRedirect('/user/register')
            else:
                LoggerUser.error(res)
                msglist.append(res[1])
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[CreateUserFromSite][%s] Exception '%(ip))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')
        
        
@never_cache
def AuthenticateUserFromEmail(HttpRequest,token,refs):
    au_user = UserFunctions.UserFnx()
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = []
    try:
        res = au_user.AuthenticateUserFromSite(token, ip)
        result = res[0]
        if( result['result'] >= 1 ):
            encrypt = Encrypt()
            return HttpResponseRedirect('/user/login/')
        else:
            msglist.append(res[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[AuthenticateUserFromEmail][%s] Exception token=%s'%(ip,token))
        msglist.append('Some Error has occoured')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')
    
        



def MessageIndex(request,message):
    encrypt = Encrypt()
    return render_to_response("txMisc/Message.html",{'message':encrypt.decrypt(message)},context_instance=RequestContext(request))    


def ListUsers(request):
    return render_to_response("txUser/ListUsers.html",{'title':'list users', 'users':User.objects.all()},context_instance=RequestContext(request))


def CreateUserIndex(request):
    return render_to_response('UserSystem/user/CreateUser.html',{'title':'create user page'},context_instance=RequestContext(request))


# HELPER FUNCTION

#FOLLOWING FUNCTION LOGS OUT A USER
def CheckAndlogout(HttpRequest):
    msglist = []
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        if "details" in HttpRequest.session.keys():
            token = HttpRequest.session['details']
            LoggerUser.debug('[CheckAndlogout][%s]logging out user, %s'%(ip,str(token)))
            logout_user = UserFunctions.UserFnx()
            res =  logout_user.LogoutUser(token['loginid'],10)
            result = res[0]
            if( result['result'] == 1):
                del HttpRequest.session['details']
                msglist.append('User logged out sucessfully.')
            else:
                LoggerUser.error("[CheckAndlogout][%s] token = %s, and result = %s"%(ip,str(token),str(result)))
                del HttpRequest.session['details']
        return msglist
    except:
        LoggerUser.exception('[CheckAndlogout][%s] Exception'%(ip))
        return []


@never_cache
def view_dashboard(HttpRequest):
    msglist = []
    try:
    #print 'i am here, i have come here', HttpRequest.session.keys()
        if "details" in HttpRequest.session:
        #return HttpResponse(str(HttpRequest.session["details"]))
            return render_to_response('txUser/home.html',{"details":str(HttpRequest.session["details"]), 'msglist':msglist},context_instance=RequestContext(HttpRequest))
        else:
            return HttpResponseRedirect('/user/login/')
    except:
        ExceptionLog.UserExceptionLog(HttpRequest.META['REMOTE_ADDR'], 'view_dashboard')
        return render_to_response('txUser/ErrorPage.html',{},context_instance=RequestContext(HttpRequest))
