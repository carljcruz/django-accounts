from django.urls import path

from . import views

urlpatterns = [

    path('order/', views.createOrder, name='order'),
    path('update/<int:pk>', views.updateOrder, name='update'),
    path('delete/<int:pk>', views.deleteOrder, name='delete'),

]
