# Create your views here.

# ListUserContact
# AddUserContactIndex
# EditUserContactIndex
# AddUserContact
# EditUserContact
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from ThoughtXplore.UserContact.BusinessFunctions.UserContactFunctions import UserContactFnx
from ThoughtXplore.CONFIG import LOGGER_USER, SESSION_MESSAGE
from ThoughtXplore.txMisc.LoggerFunctions import AppendMessageList
import logging

LoggerUser = logging.getLogger(LOGGER_USER)

def ListUserContact(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        userid = getUserId(HttpRequest)
        if( userid[0] != 1):
            LoggerUser.error('[%s] %s'%('ListUserContact',userid[1]))
            msglist.append(userid[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/login/')
        else:
            userid = userid[1]
            UserContactObj = UserContactFnx()
            result = UserContactObj.getUserContactObjectByUserid(userid)
            if result[0] != 1:
                LoggerUser.error('[%s] %s'%('ListUserContact',result[1]))
                msglist.append(result[1])
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/message/')
            ContactInfo = result[1]
            if ContactInfo is None:
                msglist.append('No contact information for this user could be found. Please user add contact page to add some details first')
            LoggerUser.debug('[%s] userid=%s, details=%s'%('ListUserContact',userid,ContactInfo))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('ProfileSystem/UserContact/EditUserContact.html',{"readonly":"true","ContactInfo":ContactInfo},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[ListUserContact][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def AddUserContactIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response('ProfileSystem/UserContact/AddUserContact.html',{},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[AddUserContactIndex][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def EditUserContactIndex(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        userid = getUserId(HttpRequest)
        if( userid[0] != 1):
            LoggerUser.error('[%s] %s'%('ListUserContact',userid[1]))
            msglist.append(userid[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/login/')
        else:
            userid = userid[1]
            UserContactObj = UserContactFnx()
            result = UserContactObj.getUserContactObjectByUserid(userid)
            if result[0] != 1:
                LoggerUser.error('[%s] %s'%('ListUserContact',result[1]))
                msglist.append(result[1])
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/message/')
            ContactInfo = result[1]
            if ContactInfo is None:
                msglist.append('No contact information for this user could be found. Please user add contact page to add some details first')
            LoggerUser.debug('[%s] userid=%s, details=%s'%('ListUserContact',userid,ContactInfo))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('ProfileSystem/UserContact/EditUserContact.html',{"readonly":"false","ContactInfo":ContactInfo},context_instance=RequestContext(HttpRequest))

    except:
        LoggerUser.exception('[EditUserContactIndex][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def AddUserContact(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        pass
    except:
        LoggerUser.exception('[AddUserContact][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def EditUserContact(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        pass
    except:
        LoggerUser.exception('[EditUserContact][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
# HELPER FUNCTIONS

def getUserId(HttpRequest):
    try:
        if "details" in HttpRequest.session.keys():
            token = HttpRequest.session["details"]
            return (1,token['userid'])
        else:
            return (-1,'user not logged in')
    except:
        LoggerUser.exception('EXCEPTION IN UserContextProcessor')
        return (-1,'Error fetching details and checking authenticity of user')