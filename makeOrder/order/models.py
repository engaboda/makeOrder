from django.db import models

# Create your models here.
class Order(models.Model):
    order_type = models.CharField(max_length=200)
    price      = models.CharField(max_length=200)
    def __str__(self):
        return self.order_type + "has price " +  self.price
