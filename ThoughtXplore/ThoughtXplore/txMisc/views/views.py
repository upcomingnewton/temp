from django.http import HttpResponse
from django.template import RequestContext , loader
from django.shortcuts import render_to_response


def ErrorHandler(HttpRequest):
    return render_to_response('txUser/ErrorPage.html',{},context_instance=RequestContext(HttpRequest))

def test(request):
    return render_to_response('test/test.html',{'title':'test page'},context_instance=RequestContext(request))