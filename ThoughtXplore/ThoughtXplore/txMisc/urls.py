from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('',
                    
                    url(r'^contenttypes/$','txMisc.views.ContentTypeViews.ListContentTypes'),
                    url(r'^contenttypes/edit/$','txMisc.views.ContentTypeViews.EditContentTypes'),
                    
                    url(r'^states/list/$','txMisc.views.StateViews.ListStates'),
                    url(r'^states/create/$','txMisc.views.StateViews.CreateStateIndex'),
                    url(r'^states/create/new/$','txMisc.views.StateViews.CreateState'),
                    
                    url(r'^perms/list/$','txMisc.views.PermissionViews.ListPermission'),
                    url(r'^perms/create/$','txMisc.views.PermissionViews.CreatePermissionIndex'),
                    url(r'^perms/create/new/$','txMisc.views.PermissionViews.CreatePermission'),
                    
                    url(r'^contenttypes/(?P<cid>\d+)/state/$','txMisc.views.StateViews.ListContentTypeStates'),
                    url(r'^contenttypes/(?P<cid>\d+)/state/edit/$','txMisc.views.StateViews.EditContentTypeStates'),
                    url(r'^contenttypes/(?P<cid>\d+)/perm/$','txMisc.views.PermissionViews.ListContentTypePermissions'),
                    url(r'^contenttypes/(?P<cid>\d+)/perm/edit/$','txMisc.views.PermissionViews.EditContentTypePermissions'),
                    url(r'^contenttypes/(?P<cid>\d+)/GroupSecurity/$','txMisc.views.PermissionViews.CreatePermission'),
                    url(r'^contenttypes/(?P<cid>\d+)/GroupSecurity/edit/$','txMisc.views.PermissionViews.CreatePermission'),
            )
