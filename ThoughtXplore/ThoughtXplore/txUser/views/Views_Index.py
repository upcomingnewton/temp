from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from ThoughtXplore.txLogging import ExceptionLog
from ThoughtXplore.txUser.views.Views_MiscFnx import CheckAndlogout

def Login_index(HttpRequest):
    msglist = []
    try:
        CheckAndlogout(HttpRequest)
        return render_to_response('txUser/Login.html',{'title':'Login','msglist':msglist},context_instance=RequestContext(HttpRequest))
    except:
        ExceptionLog.UserExceptionLog(HttpRequest.META['REMOTE_ADDR'], 'Login_index')
        return render_to_response('txUser/ErrorPage.html',{},context_instance=RequestContext(HttpRequest))


