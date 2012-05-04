    # Create your views here.
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import RequestContext , loader
from django.shortcuts import render_to_response, redirect
import datetime
from ThoughtXplore.txMisc.Validation.Validation import EmailValidate , StringValidate
from ThoughtXplore.txMisc.Encryption.enc_dec import Encrypt
from ThoughtXplore.txMenu.BusinessFunctions.MenuFunctions import  MenuFnx
from ThoughtXplore.CONFIG import LOGGER_USER, SESSION_MESSAGE
import logging
from ThoughtXplore.txMisc.Logging.LoggerFunctions import AppendMessageList
LoggerUser = logging.getLogger(LOGGER_USER)


# INDEX FUNCTIONS
def CreateMenuFromSite_Index(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    ip = HttpRequest.META['REMOTE_ADDR']
    try:
        menuobj = MenuFnx()
        parentmenu = menuobj.getParentMenus()
        if ( parentmenu[0] == 1 ):
            menulist = parentmenu[1]
            if( len(menulist) == 0):
                msglist.append('There are no parent menu items yet')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return render_to_response('UserSystem/menu/CreateMenu.html',{'title':'create menu','par_menu':menulist},context_instance=RequestContext(HttpRequest))
        else:
            LoggerUser.error("ERROR: " + parentmenu[1])
            msglist.append("ERROR: " + parentmenu[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    except:
        LoggerUser.exception('[MenuCreate_Index][%s]exception message'%(ip))
        msglist.append('Some error has occoured while processing your request')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/error/')


# CREATE MENU FUNCTIONS
def CreateMenuFromSite(HttpRequest):
    msglist = AppendMessageList(HttpRequest)
    menuobj = MenuFnx()
    ip = HttpRequest.META['REMOTE_ADDR']
    parentmenu = menuobj.getParentMenus()
    if ( parentmenu[0] == -1 ):
            msglist.append("ERROR: " + parentmenu[1])
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/error/')
    try:
        strval = StringValidate()
        menuname = HttpRequest.POST['CreateMenu_name']
        #if( strval.validate_alphanumstring( menuname) != 1 ):
        #    msglist.append('Error in menuname')
        menudesc = HttpRequest.POST['CreateMenu_desc']
        #if( strval.validate_alphanumstring( menudesc) != 1 ):
        #    msglist.append('Error in menudesc')
        menuurl = HttpRequest.POST['CreateMenu_url']
        #if( strval.validate_alphanumstring( menuurl) != 1 ):
        #    msglist.append('Error in menuurl')
        #menuicon = HttpRequest.POST['CreateMenu_micon']
        #if( strval.validate_alphastring( menuicon) != 1 ):
        #    errorlist.append('Error in menuicon')
        menuicon = 'NULL'
        menupid = -1
        if( len(parentmenu[1]) == 0 ):
            menupid = -1
        else:
            menupid  = HttpRequest.POST['CreateMenu_parmenu']
        if len(msglist) > 0:
            msglist.append('PLEASE CORRECT THESE ERRORS')
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/menu/create/')
        else:
            res = menuobj.CreateMenuFromSite(menuname, menudesc, menuurl, menupid, menuicon,1,HttpRequest.META['REMOTE_ADDR'])
            msglist.append('result code : %s , message %s'%(res[0],res[1]))
            HttpRequest.session[SESSION_MESSAGE] = msglist
            return HttpResponseRedirect('/user/menu/create/')
    except KeyError as msg:
        LoggerUser.exception('[CreateMenuFromSite][%s]exception message'%(ip))
        msglist.append(str(msg))
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/menu/create/')    
    except:
        LoggerUser.exception('[CreateMenuFromSite][%s]exception message'%(ip))
        msglist.append('exception happened in create menu function')
        HttpRequest.session[SESSION_MESSAGE] = msglist
        return HttpResponseRedirect('/user/menu/create/')

def index_edit(request,menuid):
    menuobj = MenuFnx()
    msglist = AppendMessageList(HttpRequest)
    p = menuobj.getSingleMenuItemById(menuid)
    if( len(p) == 0 ):
        msglist.append('could not fetch menu details. Please try after sometime')
    parentmenu = menuobj.getParentMenus()
    if ( len(parentmenu) == 0 ):
        msglist.append('There are no parent menu items yet')
    return render_to_response('txadmin/CreateMenu.html',{'title':'create menu','par':parentmenu,'msglist':msglist},context_instance=RequestContext(request))


def EditMenuFromSite(request):
    return HttpResponse("view page")



def ListMenu(HttpRequest,req_type):
    msglist = AppendMessageList(HttpRequest)
    menuobj = MenuFnx()
    menu = menuobj.getAllMenu()
    if len(menu) == 0 :
        msglist.append('No Menu items exist in the system')
    return render_to_response('txadmin/ListMenu.html',{'title':'list menu','menulist':menu,'msglist':msglist},context_instance=RequestContext(HttpRequest))