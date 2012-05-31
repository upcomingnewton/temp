from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response
from ThoughtXplore.CONFIG import LOGGER_MISC,SESSION_MESSAGE
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
from ThoughtXplore.txMisc.BusinessFunctions.States import StatesClass
import logging

LoggerMisc = logging.getLogger(LOGGER_MISC)

def  ListStates(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        stateobj = StatesClass()
        statelist = stateobj.getAllStates()
        if statelist[0] == 1:
            statelist = statelist[1]
            if len(statelist) == 0:
                msglist.append('There are no states defined yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/states/EditStates.html',{'statelist':statelist,'visible_list':'true','visible_create':'false',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListStates',ip))
            msglist.append('[ERROR][ListStates] %s'%(statelist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListStates',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
    
def ListContentTypeStates(HttpRequest,cid):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        stateobj = StatesClass()
        statelist = stateobj.getAllStatesForAContentTypeBYID(cid)
        if statelist[0] == 1:
            statelist = statelist[1]
            if len(statelist) == 0:
                msglist.append('There are no states defined for this content type yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/states/EditStates.html',{'statelist':statelist,'visible_list':'true','visible_create':'false',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListStates',ip))
            msglist.append('[ERROR][ListStates] %s'%(statelist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListStates',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
def CreateStateIndex(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        return render_to_response('security/states/EditStateContentType.html',{'visible_list':'false','visible_create':'true',},context_instance=RequestContext(HttpRequest))
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('CreateStateIndex',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def CreateState(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        name = ''
        desc = ''
        if 'EditStateCreate_Name' in HttpRequest.POST:
            name = HttpRequest.POST['EditStateCreate_Name']
            if len(name) < 1:
                msglist.append('Proper Name required')
        else:
            msglist.append('Name required')
        if 'EditStateCreate_Desc' in HttpRequest.POST:
            desc = HttpRequest.POST['EditStateCreate_Desc']
            if len(desc) < 1:
                msglist.append('Proper Desc required')
        else:
            msglist.append('Desc required')
        if len(msglist) > 0:
            msglist.append('PLEASE CORRECT THESE ERRORS')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/admin/security/states/create/')
        else:
            StatesClassObj = StatesClass()
            res = StatesClassObj.CreateState(name, desc, by, ip)
            msglist.append('result code : %s , message %s'%(res[0],res[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/group/create/')
    except KeyError as msg:
        LoggerMisc.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append(str(msg))
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/admin/security/states/create/')
    except:
        LoggerMisc.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append('exception happened in create group function')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')


