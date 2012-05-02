from ThoughtXplore.CONFIG import SESSION_MESSAGE
import sys

def CheckAndMakeMessageSession(HttpRequest,msglist):
    if len(msglist) > 0:
        try:
            if SESSION_MESSAGE in HttpRequest.session.keys():
                HttpRequest.session[SESSION_MESSAGE] = msglist
            else:
                HttpRequest.session[SESSION_MESSAGE] = msglist
        except:
            print sys.exc_info()