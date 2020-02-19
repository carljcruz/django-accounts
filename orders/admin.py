from django.contrib import admin
from orders.models import Order

admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
