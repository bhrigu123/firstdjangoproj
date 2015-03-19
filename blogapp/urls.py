from django.conf.urls import patterns, url
from blogapp import views

urlpatterns = patterns('',
	url(r'^$', views.blogs, name='index'),
	url(r'^(?P<blog_id>\d+)/$', views.blog_detail,name='detail'),
)