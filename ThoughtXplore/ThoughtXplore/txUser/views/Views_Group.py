from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext , loader
from django.shortcuts import render_to_response, redirect
from ThoughtXplore.txUser.models import User, Group
from ThoughtXplore.txUser.BusinessFunctions.UserFunctions import UserFnx
import datetime
from ThoughtXplore.txMisc.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.enc_dec import Encrypt
from django.core.urlresolvers import reverse
from ThoughtXplore.txCommunications.CommunicationFunctions import send_validation_email
from ThoughtXplore.txMisc import enc_dec
from ThoughtXplore.txMenu.BusinessFunctions.MenuFunctions import MenuFnx
from ThoughtXplore.txUser.BusinessFunctions.GroupFunctions import GroupFnx
from ThoughtXplore.CONFIG import LOGGER_USER, SESSION_MESSAGE
import logging
from ThoughtXplore.txMisc.LoggerFunctions import AppendMessageList
LoggerUser = logging.getLogger(LOGGER_USER)

def ListGroups(HttpRequest, req_type):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        
        if req_type == "all":
            group = GroupFnx()
            grouplist = group.ListAllGroups()
            if( grouplist[0] == 1 ):
                grouplist = grouplist[1]
                if ( len(grouplist) == 0):
                        msglist.append("THERE NO GROUPS IN THE SYSTEM, YET")
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return render_to_response('UserSystem/GROUP/ListGroups.html',{'grouplist':grouplist},context_instance=RequestContext(HttpRequest))
            else:
                LoggerUser.error('[%s] req_type = %s, return code = %s, ip = %s'%('ListGroups',req_type,str(grouplist),ip))
                msglist.append('[ERROR][ListGroups] %s'%(grouplist[1]))
                HttpRequest.session[SESSION_MESSAGE] = msglist
                return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[%s] req_type = %s, ip = %s'%('ListGroups',req_type,ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')


def CreateGroup_Index(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return render_to_response('UserSystem/GROUP/CreateGroup.html',{},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[CreateGroup_Index][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')
   
def CreateGroup(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        gname = HttpRequest.POST['Group_Name']
        if gname is None:
            msglist.append("ERROR : group name is required")
        gdesc = HttpRequest.POST['Group_Desc']
        if gdesc is None:
                msglist.append("ERROR: group desc is required")
        if len(msglist) > 0:
            msglist.append('PLEASE CORRECT THESE ERRORS')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/group/create/')
        else:
            group_obj = GroupFnx()
            res = group_obj.CreateGroup(gname, gdesc, 1, 'system', 1, ip)
            msglist.append('result code : %s , message %s'%(res[0],res[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/group/create/')
    except KeyError as msg:
        LoggerUser.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append(str(msg))
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/group/create/')  
    except:
        LoggerUser.exception('[CreateGroup][%s]exception message'%(ip))
        msglist.append('exception happened in create group function')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/group/create/')

def AddUsers_Index(HttpRequest,gid):
    msglist = []
    #userobj = User()
    userlist = User.objects.all()
    if len(userlist) == 0:
        msglist.append("ERROR !!! there are no users in the system yet.")
    return render_to_response('txadmin/EditGroupUsers_AddUsers.html',{'msglist':msglist,'userlist':userlist, 'groupid':gid},context_instance=RequestContext(HttpRequest))

def EditUsers_Index(HttpRequest,gid):
    return HttpResponseRedirect("/user/group/" + str(gid) + "/users/add/")
    
    
def AddUsersToGroup(HttpRequest,gid):
    userlist = HttpRequest.POST.getlist('Group_Userid')
    group = GroupFnx()
    group.AddUserToGroup(gid, userlist, 1, 'test')