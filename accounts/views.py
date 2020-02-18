from django.shortcuts import render
from django.http import HttpResponse



def homepage(request):
    template_name = 'profile.html'
    return render(request, template_name, {})
def createUser(request):
    return HttpResponse('Create page')

def loginUser(request):
    return HttpResponse('Login Page')

def logoutUser(request):
    return HttpResponse('Logout Page')

