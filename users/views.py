from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from .models import *
from .forms import *

def index(request):
    context ={'Status':'working'}
    return render(request, "index.html", context)



@login_required(login_url='login')    
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, "account.html", context)

def login_page(request):
    page = 'login'
    if request.method == 'POST':
        user = authenticate(
            email=request.POST['email'],
        password=request.POST['password']
        )
        if user is not None :
            login(request, user)
            return redirect('homepage')

    context = {'page':page}
    return render(request,"authenticate.html",context)

def logout_f(request):
    logout(request)
    return redirect('login')


def register_page(request):
    form = CustomUserCreationForum
    if request.method == 'POST':
        form = CustomUserCreationForum(request.POST)
        if form.is_valid():
                form.save()
                return redirect('login')
    page = 'register'
    context = {'page':page, 'form': form}
    return render(request,"authenticate.html",context)   



@login_required(login_url='login')    
def account(request):
    user = request.user
    context = {'user': user}
    return render(request, "account.html", context)
