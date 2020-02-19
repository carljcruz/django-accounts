from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def createOrder(request):
    template_name = 'create_order.html'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('profile')

    context = {
        'form': form
    }
    return render(request,template_name, context)



def updateOrder(request, pk):
    template_name = 'update_order.html'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('profile')

    context = {
        'form': form
    }
    return render(request, template_name, context)


def deleteOrder(request, pk):
    template_name = 'delete_order.html'
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('profile')
    context = {
        'order':order
    }
    return render(request, template_name, context)




