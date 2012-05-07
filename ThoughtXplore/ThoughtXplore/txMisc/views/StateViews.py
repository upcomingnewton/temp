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
            return render_to_response('security/states/EditStates.html',{'statelist':statelist,'can_edit':'true','visible_list':'true','visible_edit':'false','visible_create':'false',},context_instance=RequestContext(HttpRequest))
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
#CreateStateIndex
#CreateState
#EditStateIndex,stateid
#EditState,stateid

