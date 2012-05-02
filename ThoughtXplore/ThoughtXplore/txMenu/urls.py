from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
                       
       #group menu functions
       url(r'^group/(?P<gid>\d+)/menu/list/$','txMenu.views.GroupMenu.ListGroupMenu_Index'),
       url(r'^group/(?P<gid>\d+)/menu/edit/$','txMenu.views.GroupMenu.EditGroupMenu_Index'),
       url(r'^group/(?P<gid>\d+)/menu/edit/new/$','txMenu.views.GroupMenu.EditGroupMenu'),
                       
                         
        # menu functions
        url(r'^menu/create/$','txMenu.views.Menu.CreateMenuFromSite_Index'),
        url(r'^menu/create/new/$','txMenu.views.Menu.CreateMenuFromSite'),
        url(r'^menu/(?P<menuid>\d+)/edit/$','txMenu.UserViews.index_edit'),
        url(r'^menu/(?P<menuid>\d+)/edit/update/$','txMenu.UserViews.EditMenuFromSite'),
        url(r'^menu/list/(?P<req_type>\S+)/$','txMenu.UserViews.ListMenu'),
        url(r'^menu/edit/many/$','txMenu.UserViews.ListMenu'),
    )  