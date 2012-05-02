#user has logged in sucessfully
#1. determmine it's group 
#2. check if menu is available for this group in cache or not 

#5. make the menu system for this user
#7. redirect the user to dashboard page
from django.core.cache import cache
import ThoughtXplore.CONFIG as CONFIG
from ThoughtXplore.txMenu.BusinessFunctions.GroupMenuFunctions import GroupMenuFunctions
from ThoughtXplore.CONFIG import LOGGER_USER, CACHE_TIME_FOR_GROUP_MENU
import logging

LoggerUser = logging.getLogger(LOGGER_USER)

def MakeGroupMenu(groupid):
    try:
        groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
        LoggerUser.debug('[%s] group key is : %s'%('MakeGroupMenu',groupkey))
        #test_cache("testkey","testvalue")
        if cache.get(groupkey) is None:
            LoggerUser.debug('[%s] key is not in cache'%('MakeGroupMenu'))
            to_cache = MakeGroupMenuCache(groupid)
            cache.add(groupkey,to_cache,CACHE_TIME_FOR_GROUP_MENU)
            return to_cache
        else:
            LoggerUser.debug('[%s] cache is there :-)'%('MakeGroupMenu'))
            return cache.get(groupkey)
    except:
        LoggerUser.exception('[%s] exception'%('MakeGroupMenu'))
        return []
    
def test_cache(key,val):
    if cache.get(key) is None:
        LoggerUser.debug('[%s] group key is : %s is *** NO NO *** there in cache, adding'%('test_cache',key))
        cache.add(key,val,CACHE_TIME_FOR_GROUP_MENU)
    else:
        LoggerUser.debug('[%s] group key is : %s is  there in cache, adding'%('test_cache',key))
    
        
def ResetGroupMenu(groupid):
    try:
            groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
            ClearGroupMenuCache(groupid)
            to_cache = MakeGroupMenuCache(groupid)
            cache.set(groupkey,to_cache)
    except:
        LoggerUser.exception('[%s] exception'%('ResetGroupMenu'))
        
        
def ClearGroupMenuCache(groupid):
    try:
        groupkey = CONFIG.GROUP_MENU_PREFIX + str(groupid)
        if cache.get(groupkey) is not None:
            cache.delete(groupkey)
    except:
        LoggerUser.exception('[%s] exception'%('ResetGroupMenu'))
        
def MakeGroupMenuCache(groupid):
    try:
        LoggerUser.debug( 'inside MakeGroupMenuCache gid = %s'%groupid);
        ClearGroupMenuCache(groupid)
        final_result = []
        temp = []
        grpmenu_obj = GroupMenuFunctions()
        menus = grpmenu_obj.GetAllMenuObjectsByGroupid(groupid)
        if( menus[0] == 1):
            menus = menus[1]
            for menu in menus:
                temp = []
                if menu.MenuPid == -1:
                    temp.append(menu)
                    for x in menus:
                        if x.MenuPid == menu.id:
                            temp.append(x)
                    #if ( len(temp) > 0):
                    #    temp.append(menu)
                if( len(temp) > 0 ):
                    final_result.append(temp)
        LoggerUser.debug('final list is %s'% (str(final_result)))
        return final_result
    except:
        LoggerUser.exception('[%s] exception'%('ResetGroupMenu'))
        return []