from django.contrib import admin
from .models import Blogs, blogpostComment,Contact, ContactMe
# Register your models here.
admin.site.register((Blogs, blogpostComment,Contact,ContactMe))