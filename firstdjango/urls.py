"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404, include
from django.contrib import admin
from django.urls import path

admin.site.site_header = "Ayush blog admin"
admin.site.site_title = "Ayush blogs"
admin.site.index_title = "Welcome to ayush blogs admin panel"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('forn.urls') )
]

handler404 = 'forn.views.error_404'