from django.shortcuts import render
from blogapp.models import Blog

# Create your views here.
def blogs(request):
	blog_list = Blog.objects.all()
	return render(request,'blogapp/index.html',{'bloglist': blog_list})

def blog_detail(request,blog_id):
	blog = Blog.objects.get(pk=blog_id)
	return render(request,'blogapp/content.html',{'blog':blog})