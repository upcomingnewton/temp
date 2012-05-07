from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('',
                    
                    url(r'^contenttypes/$','txMisc.views.ContentTypeViews.ListContentTypes'),
                    url(r'^contenttypes/edit/$','txMisc.views.ContentTypeViews.EditContentTypes'),
                    
                    url(r'^states/list/$','txMisc.views.StateViews.ListStates'),
                    url(r'^states/create/$','txMisc.views.StateViews.CreateStateIndex'),
                    url(r'^states/create/new/$','txMisc.views.StateViews.CreateState'),
                    url(r'^states/(?P<stateid>\d+)/edit/$','txMisc.views.StateViews.EditStateIndex'),
                    url(r'^states/(?P<stateid>\d+)/edit/state/$','txMisc.views.StateViews.EditState'),
                       )