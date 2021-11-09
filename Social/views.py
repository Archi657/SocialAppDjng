from django.shortcuts import render
from .models import *
def feed(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request,'Social/feed.html', ctx)

def profile(request):
    return render(request,'Social/profile.html')