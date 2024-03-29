from django.http import HttpResponseRedirect
from django.template import RequestContext 
from django.shortcuts import render_to_response
from ThoughtXplore.CONFIG import LOGGER_MISC,SESSION_MESSAGE
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
from ThoughtXplore.txMisc.BusinessFunctions.Permissions import PermissionsClass
import logging

LoggerMisc = logging.getLogger(LOGGER_MISC)

def  ListPermission(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        permobj = PermissionsClass()
        permlist = permobj.getAllPermissions()
        if permlist[0] == 1:
            permlist = permlist[1]
            if len(permlist) == 0:
                msglist.append('There are no permissions defined yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/permissions/EditPermission.html',{'permlist':permlist,'visible_list':'true','visible_create':'false',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListPermission',ip))
            msglist.append('[ERROR][ListPermission] %s'%(permlist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListPermission',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
def ListContentTypePermissions(HttpRequest,cid):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        permobj = PermissionsClass()
        permlist = permobj.getAllPermissionsForAContentTypeByID(cid)
        if permlist[0] == 1:
            permlist = permlist[1]
            if len(permlist) == 0:
                msglist.append('There are no permissions defined for this content type yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('security/permissions/EditPermission.html',{'permlist':permlist,'visible_list':'true','visible_create':'false',},context_instance=RequestContext(HttpRequest))
        else:
            LoggerMisc.error('[%s] ip = %s'%('ListPermission',ip))
            msglist.append('[ERROR][ListContentTypePermissions] %s'%(permlist[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/message/')
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('ListContentTypePermissions',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')
    
    
def CreatePermissionIndex(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        return render_to_response('security/states/EditPermission.html',{'visible_list':'false','visible_create':'true',},context_instance=RequestContext(HttpRequest))
    except:
        LoggerMisc.exception('[%s] EXCEPTION ip = %s'%('CreatePermissionIndex',ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')

def CreatePermission(HttpRequest):
    ip = HttpRequest.META['REMOTE_ADDR']
    msglist = AppendMessageList(HttpRequest)
    try:
        name = ''
        desc = ''
        if 'EditState_Create_Name' in HttpRequest.POST:
            name = HttpRequest.POST['EditState_Create_Name']
            if len(name) < 4:
                msglist.append('Proper Name required')
        else:
            msglist.append('Name required')
        if 'EditState_Create_Desc' in HttpRequest.POST:
            desc = HttpRequest.POST['EditState_Create_Desc']
            if len(desc) < 4:
                msglist.append('Proper Desc required')
        else:
            msglist.append('Desc required')
        if len(msglist) > 0:
            msglist.append('PLEASE CORRECT THESE ERRORS')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/admin/security/states/create/')
        else:
            PermClassObj = PermissionsClass()
            res = PermClassObj.CreatePermission(name, desc, 1, ip)
            msglist.append('result code : %s , message %s'%(res[0],res[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/admin/security/contenttypes/')
    except KeyError as msg:
        LoggerMisc.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append(str(msg))
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/admin/security/perms/create/')
    except:
        LoggerMisc.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append('exception happened in create group function')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/message/')


