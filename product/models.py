from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_type = models.CharField(max_length=100)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_quantity = models.IntegerField()
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=100)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)