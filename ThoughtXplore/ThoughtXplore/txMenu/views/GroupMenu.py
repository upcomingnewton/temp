from ThoughtXplore.txMenu.BusinessFunctions.GroupMenuFunctions import GroupMenuFunctions 
from ThoughtXplore.txMenu.BusinessFunctions.MenuFunctions import MenuFnx 
import traceback
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from ThoughtXplore.CONFIG import LOGGER_USER, SESSION_MESSAGE
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
import logging

LoggerUser = logging.getLogger(LOGGER_USER)

def ListGroupMenu_Index(HttpRequest,gid):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        groupmenu_obj = GroupMenuFunctions()
        menulist = groupmenu_obj.GetAllMenuObjectsByGroupid(gid)
        if(menulist[0] == 1):
            menulist = menulist[1]
            if(  len(menulist) == 0 ):
                msglist.append('There are no menu items assigned to this group yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('UserSystem/GroupMenu/ListGroupMenu.html',{'groupmenulist':menulist},context_instance=RequestContext(HttpRequest))
        else:
            LoggerUser.error("ERROR: " + menulist[1])
            msglist.append("ERROR: " + menulist[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[ListGroupMenu_Index][%s]exception message for gid %s'%(ip,gid))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')
        
        
def EditGroupMenu_Index(HttpRequest,gid):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        menuobj = MenuFnx()
        menulist = menuobj.getAllMenu()
        if( menulist[0] == 1):
            menulist = menulist[1]
            if(  len(menulist) == 0 ):
                msglist.append('There are no menu items assigned to this group yet')
        else:
            LoggerUser.error("ERROR: " + menulist[1])
            msglist.append("ERROR: " + menulist[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
        groupmenu_obj = GroupMenuFunctions()
        groupmenulist = groupmenu_obj.getMenuIDbyGroupIdForGroup(gid)
        if( groupmenulist[0] == 1):
            groupmenulist = groupmenulist[1]
            if(  len(groupmenulist) == 0 ):
                msglist.append('There are no groupmenulist items  yet')
        else:
            LoggerUser.error("ERROR: " + groupmenulist[1])
            msglist.append("ERROR: " + groupmenulist[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
        return render_to_response('UserSystem/GroupMenu/EditGroupMenu.html',{'groupmenulist':groupmenu_obj.SetGroupMenuForEditing(menulist, groupmenulist), 'gid':gid},context_instance=RequestContext(HttpRequest))
    except:
        LoggerUser.exception('[ListGroupMenu_Index][%s]exception message for gid %s'%(ip,gid))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')

        
def EditGroupMenu(HttpRequest,gid):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        selected_menu = HttpRequest.POST.getlist('CheckBox_EditGroupMenuOptions')
        LoggerUser.debug('[EditGroupMenu] selected menu is %s'%(selected_menu)) 
        groupmenu_obj = GroupMenuFunctions()
        result =  groupmenu_obj.CreateGroupMenu(gid, selected_menu, 1, 'test')
        if( result[0] != -1):
            msglist.append("SUCCESS" + str(result))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/group/list/all/')
        else:
            LoggerUser.error('[EditGroupMenu][%s]error message for gid %s, msg = %s'%(ip,gid,result[1]))
            msglist.append(result[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[EditGroupMenu][%s]exception message for gid %s'%(ip,gid))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')