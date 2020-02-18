from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
def homepage(request):
    template_name = 'profile.html'
    return render(request, template_name, {})


def createUser(request):
    form = RegisterUserForm()
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been created successfully')
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def loginUser(request):
    form = RegisterUserForm()
    template_name = 'login.html'

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        print(request.POST)
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password1')
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
    context = {
        'form': form,
    }
    return render(request, template_name, context)



def logoutUser(request):
    logout(request)
    template_name = 'logout.html'
    return render(request, template_name, {})
























