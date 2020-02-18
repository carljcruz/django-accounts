from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.homepage, name='profile'),
    path('register/', views.createUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
