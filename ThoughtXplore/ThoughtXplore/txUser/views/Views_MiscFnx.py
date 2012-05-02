from ThoughtXplore.txUser.BusinessFunctions.UserFunctions import UserFnx
from ThoughtXplore.txLogging import ExceptionLog


def CheckAndlogout(HttpRequest):
    if "details" in HttpRequest.session.keys():
            token = HttpRequest.session['details']
            print token
            logout_user = UserFnx()
            result =  logout_user.LogoutUser(token['loginid'])
            if( result['result'] == 1):
                del HttpRequest.session['details']
            else:
                ExceptionLog.UserErrorLog(HttpRequest.META['REMOTE_ADDR'], 'CheckAndlogout',str(result) )
                del HttpRequest.session['details']
    
