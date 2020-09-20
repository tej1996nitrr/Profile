from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'core/index.html')
def posts(request):
    return render(request, 'core/posts.html')
def post(request):
    return render(request, 'core/post.html')
# def profile(request):
#     return HttpResponse('<h2>Profile title</h2>')
