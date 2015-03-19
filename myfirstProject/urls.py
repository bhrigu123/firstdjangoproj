from django.conf.urls import patterns, include, url
from django.contrib import admin
from demoapp.views import hello, current_date, hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfirstProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #^ starts with
    #$ end..nothing more
    #r is raw string
    url(r'^hello/$',hello),
    url(r'^current_time/$', current_date),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogapp/',include('blogapp.urls', namespace='blogs')),    
) 
