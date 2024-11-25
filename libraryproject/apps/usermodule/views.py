from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

def userRegister(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'You have successfully registered')
            return redirect('books.list_books')
    else:
        form = UserRegister()
    return render(request, 'usermodule/userRegister.html', {'form': form})

def userlogin(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully')
                return redirect('books.list_books')
            else:
                form.add_error(None, "Invalid username or password")
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLogin()
    return render(request,"usermodule/userLogin.html", {'form':form})

def userLogout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('books.aboutus')