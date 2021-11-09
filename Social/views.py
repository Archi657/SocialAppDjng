from django.shortcuts import render

def feed(request):
    return render(request,'Social/feed.html')

def profile(request):
    return render(request,'Social/profile.html')