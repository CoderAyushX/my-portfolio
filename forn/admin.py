from django.contrib import admin
from .models import blogs, blogpostComment,contactUs, contactMe
# Register your models here.
admin.site.register((blogs, blogpostComment,contactUs,contactMe))