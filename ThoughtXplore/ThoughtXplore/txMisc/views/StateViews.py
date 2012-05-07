from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response
from ThoughtXplore.CONFIG import LOGGER_MISC
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
import logging

LoggerMisc = logging.getLogger(LOGGER_MISC)

def  ListStates(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    pass
#CreateStateIndex
#CreateState
#EditStateIndex,stateid
#EditState,stateid

