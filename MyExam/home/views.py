from django.shortcuts import render
# Create your views here.

def signIn(request):
    return render(request,'home/sign-in.html')

def index(request):
    return render(request,'home/index.html')

def base(request):
    return render(request,"home/base-index.html")
