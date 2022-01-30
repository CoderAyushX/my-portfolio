from django.contrib import admin
from .models import blogs, blogpostComment,Contact, ContactMe
# Register your models here.
admin.site.register((blogs, blogpostComment,Contact,ContactMe))