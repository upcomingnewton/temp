from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response

# list all content types, only list with no edit options
def ListContentTypes(HttpRequest):
    pass


# list all content types along with edit options
def EditContentTypes(HttpRequest):
    pass


def ErrorHandler(HttpRequest):
    return render_to_response('txUser/ErrorPage.html',{},context_instance=RequestContext(HttpRequest))

def test(request):
    return render_to_response('test/test.html',{'title':'test page'},context_instance=RequestContext(request))