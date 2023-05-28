from django.shortcuts import render
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

def feed(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request,'Social/feed.html', ctx)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} has been created')
    else:
        form = UserRegisterForm()
    ctx = { 'form' : form }
    return render(request, 'Social/register.html', ctx)

def profile(request):
    return render(request,'Social/profile.html')