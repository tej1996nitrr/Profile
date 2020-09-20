from django.shortcuts import render
from django.http import HttpResponse
from .models import  Skills, Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    skills = Skills.objects.all()
    context = {'posts':posts, 'skills':skills}
    
    return render(request, 'core/index.html', context)
def posts(request):
    return render(request, 'core/posts.html')
def post(request):
    return render(request, 'core/post.html')
# def profile(request):
#     return HttpResponse('<h2>Profile title</h2>')
