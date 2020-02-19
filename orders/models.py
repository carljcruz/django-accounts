from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    readonly_fields = ('date_created',)

    def __str__(self):
        return str(self.order_number)

