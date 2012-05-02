from django.conf.urls.defaults import patterns,  url


urlpatterns = patterns('',
        
        #COMMON USER FUNCTIONS
        url(r'^profile/contact/$','UserContact.views.UserContact_views.ListUserContact'),
        url(r'^profile/contact/add/$','UserContact.views.UserContact_views.AddUserContactIndex'),
        url(r'^profile/contact/edit/$','UserContact.views.UserContact_views.EditUserContactIndex'),
        
        # POST BACK FUNCTIONS
        
        url(r'^profile/contact/add/pb/$','UserContact.views.UserContact_views.AddUserContact'),
        url(r'^profile/contact/edit/pb/$','UserContact.views.UserContact_views.EditUserContact'),
        
        # ADMIN FUNCTIONS
        url(r'^admin/profile/contact/list/(?P<req_type>\S+)/$','UserContact.views.Admin_UserContact_views.ListUserContact'),
        url(r'^profile/contact/add/$','UserContact.views.Admin_UserContact_views.AddUserContactIndex'),
        url(r'^profile/contact/edit/$','UserContact.views.Admin_UserContact_views.EditUserContactIndex'),
        url(r'^admin/profile/(?P<profile_id>\d+)/contact/add/$','UserContact.views.Admin_UserContact_views.AddUserContact'),
        url(r'^admin/profile/(?P<profile_id>\d+)/contact/edit/$','UserContact.views.Admin_UserContact_views.EditUserContact'),
)               