from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class blogs(models.Model):
    date = models.DateTimeField( auto_now_add=True)
    title = models.CharField(max_length= 150)
    content = models.TextField()
    slug = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class blogpostComment(models.Model):
    IDno = models.AutoField(primary_key=True )
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blogs, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null= True)
    timestamp = models.DateTimeField(default= now)
    def __str__(self):
        return self.comments[0:15] + "....."  + ' by ' + self.user.username

class contactUs(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    message = models.TextField()
    def __str__(self):
        return self.firstName

        
class contactMe(models.Model):
    gmail = models.EmailField(max_length=254)
    message = models.TextField()