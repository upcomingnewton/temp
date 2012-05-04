from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('',
                    
                    url(r'^contenttypes/$','txMisc.views.ContentTypeViews.ListContentTypes'),
                    url(r'^contenttypes/edit/$','txMisc.views.ContentTypeViews.EditContentTypes'),
                       )