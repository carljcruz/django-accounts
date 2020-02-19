from .forms import RegisterUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from orders.models import Order



def homepage(request):
    template_name = 'profile.html'
    order = Order.objects.filter(user=request.user)
    if request.user.is_anonymous:
        messages.info(request, 'You must be logged in to view that page')
        return redirect('login')

    context = {
        'orders': order
    }
    return render(request, template_name, context)


def createUser(request):
    form = RegisterUserForm()
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"Your account <u>{username}</u> has been"
                          f" successfully created", extra_tags='safe')
            return redirect('register')

    context = {
        'form': form,
    }
    return render(request, template_name, context)

def loginUser(request):
    form = RegisterUserForm()
    template_name = 'login.html'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
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
























