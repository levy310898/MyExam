from django.shortcuts import render
# Create your views here.

def signIn(request):
    return render(request,'home/sign-in.html')

<<<<<<< HEAD
def index(request):
=======
def signUp(request):
    return render(request, 'home/sign-up.html')

def index(request,user):
>>>>>>> 8d1ae608a16b788724c1b22c345bf2b4d889e946
    return render(request,'home/index.html')

def base(request):
    return render(request,"home/base-index.html")
