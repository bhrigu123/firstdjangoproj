from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime
from blogapp.models import Blog, Comments


# Create your views here.
def hello(request):
	#returning smth
	print(request)
	return HttpResponse("Hello World!")
def current_date(request):
	now = datetime.datetime.now()
	html = "<html><head><title>Current Time</title></head><body> It is now %s </body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><head><title>Current Time</title></head><body> In %s hours, time will be %s </body></html>" % (offset,dt)
	return HttpResponse(html)

def blogs(request):
	blog_list = Blog.objects.all()
	return render(request,'blogapp/index.html',{'bloglist': blog_list})