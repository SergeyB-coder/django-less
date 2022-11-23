from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Posts


# Create your views here.

# ГЛАВНАЯ
def index(request):
    return render(request, 'home.html')

# ПРОФИЛЬ
def profile(request):
    return render(request, 'profile.html')

# POSTS
def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# NEWPOST
def newpost(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    file = request.FILES['file']
    fss = FileSystemStorage('appshop/static/images/')
    saved_file = fss.save(file.name, file)
    
    post = Posts()
    post.title = title
    post.text = text
    post.image = file.name
    post.save()
    return HttpResponseRedirect('/posts')

def postinfo(request, id):
    post = Posts.objects.get(id=id)
    return render(request, 'postinfo.html', {'post': post})


