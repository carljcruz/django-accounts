from django.contrib import admin
from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    list_display = ['order_number', 'customer_name', 'date_created', 'user']
    fields = ('order_number', 'customer_name', 'date_created', 'user')

admin.site.register(Order, OrderAdmin)

