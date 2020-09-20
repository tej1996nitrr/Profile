from django.shortcuts import render
from django.http import HttpResponse
from .models import  Skills, Post
from .filters import  PostFilter

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:6]
    skills = Skills.objects.all()
    context = {'posts':posts, 'skills':skills}
    
    return render(request, 'core/index.html', context)

def posts(request):
    posts = Post.objects.all()
    myfilter = PostFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    context = {'posts':posts, 'myfilter': myfilter}

    return render(request, 'core/posts.html', context)

def post(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'core/post.html', context)
# def profile(request):
#     return HttpResponse('<h2>Profile title</h2>')
