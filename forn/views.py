from django.contrib import auth,messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
# Create your views here.
def index(request):    
    return render(request, 'index.html')
def contactMe(request):
    try:
      if request.method == "POST":
        gmails = request.POST['gmail']
        messages = request.POST['message']
        contactme = ContactMe(gmail= gmails,  message= messages)
        contactme.save()
        return redirect('/')
    except:
      return redirect('contact')

def contact(request):
    if request.method == "POST":
        Fname = request.POST.get('name')
        Lname = request.POST.get('lastName')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        contact = Contact(firstName= Fname , lastName= Lname, email= email , mobile= mobile, message= message)
        contact.save()
        messages.info(request,"Message sent sucessfully")
    return render(request, 'contact.html')
def blog(request):
    blog = Blogs.objects.all()
    return render(request, 'blog.html' , {"blogs": blog})
def signup(request):
    if request.method == 'POST':
        username = request.POST['fullname']
        email =  request.POST['email']
        password =  request.POST['password']
        password2 =  request.POST['password2']
        firstname =""
        lastname = ""
        namelist = username.split()
        lname = namelist[len(namelist)- 1]
        if namelist[0] == lname:
            firstname += namelist[0]
            lastname += " "
        else:
            firstname += namelist[0]
            lastname += lname
        if password == password2:
            if User.objects.filter(username = username).exists():
                  messages.info(request, "User name is taken")
                  return redirect('signup')
            elif User.objects.filter(email = email).exists():
                 messages.info(request, "email alredy in use")
                 return redirect('signup')
            else:
                 user = User.objects.create_user(username = username, password = password, email= email ,first_name =firstname, last_name = lastname)
                 user.save()
                 return render(request, 'login.html')

    else:
         return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        user = auth.authenticate(username =username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"User not exist")
            return redirect('login')
    else:
      return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
def blogpost(request, slug):
    post = Blogs.objects.filter(slug= slug).first()
    comments = blogpostComment.objects.filter(post = post)
    relatedPost = Blogs.objects.all().exclude(id= post.id)[:4]
    return render(request, 'blogpost.html', {'posts':post, 'comment': comments, 'relatedpost': relatedPost})

def comment(request):
    if request.user.is_anonymous:
        return redirect('/signup')
    if request.method == "POST":
         comment = request.POST.get('comment')
         user = request.user
         postno  =  request.POST.get('Sno')
         post = Blogs.objects.get(id = postno)
         comment = blogpostComment(comments= comment, user= user, post= post)
         comment.save()
    return redirect(f'/blog/{post.slug}')

def error_404(request, exception):
    return render(request, '404.html')
