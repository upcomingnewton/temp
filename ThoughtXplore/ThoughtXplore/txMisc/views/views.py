from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response



def ErrorHandler(HttpRequest):
    return render_to_response('txUser/ErrorPage.html',{},context_instance=RequestContext(HttpRequest))