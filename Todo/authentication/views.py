from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def LogIn(request):
    if request.method == "POST":
        u_name = request.POST['username']
        u_password = request.POST['password']

        user=authenticate(username=u_name,password=u_password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("wrong Credentials")

    return render(request,'LogIn.html')

def Register(request):
    if request.method == "POST":
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        u_email = request.POST['email']
        u_name = request.POST['username']
        u_password = request.POST['password']

        u=User.objects.create(first_name=f_name,last_name=l_name,email=u_email ,username=u_name)
        u.set_password(u_password)
        u.save()
        return redirect('LogIn')

    return render(request,'Register.html')

def LogOut(request):
    logout(request)
    return render(request,'LogIn.html')
    