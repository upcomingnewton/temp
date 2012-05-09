from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response
from ThoughtXplore.CONFIG import LOGGER_MISC,SESSION_MESSAGE
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
from ThoughtXplore.txMisc.BusinessFunctions.ContentTypes import ContentTypeClass
import logging

LoggerMisc = logging.getLogger(LOGGER_MISC)

# list all content types, only list with no edit options
def ListContentTypes(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        ctobj = ContentTypeClass()
        ctlist = ctobj.getAllContentTypes()
        if ctlist[0] == 1:
            ctlist = ctlist[1]
            if len(ctlist) == 0:
                msglist.append('There are no content types defined yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/contenttypes/ContentType.html',{'ctlist':ctlist,'can_edit':'false',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListContentTypes',ip))
            msglist.append('[ERROR][ListContentTypes] %s'%(ctlist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListContentTypes',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')


# list all content types along with edit options
def EditContentTypes(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        ctobj = ContentTypeClass()
        ctlist = ctobj.getAllContentTypes()
        if ctlist[0] == 1:
            ctlist = ctlist[1]
            if len(ctlist) == 0:
                msglist.append('There are no content types defined yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/contenttypes/ContentType.html',{'ctlist':ctlist,'can_edit':'true',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListContentTypes',ip))
            msglist.append('[ERROR][ListContentTypes] %s'%(ctlist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListContentTypes',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')




def test(request):
    return render_to_response('test/test.html',{'title':'test page'},context_instance=RequestContext(request))