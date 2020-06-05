from django.shortcuts import render
# Create your views here.

def signIn(request):
    return render(request,'home/sign-in.html')

def signUp(request):
    return render(request, 'home/sign-up.html')

def index(request,user):
    return render(request,'home/index.html')
