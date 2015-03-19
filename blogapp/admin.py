from django.contrib import admin

# Register your models here.
from blogapp.models import Blog,Comments
admin.site.register(Blog)
admin.site.register(Comments)