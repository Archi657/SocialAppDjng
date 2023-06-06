from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import UserRegisterForm, PostForm
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

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', {'form':form})


def profile(request):
    return render(request,'Social/profile.html')