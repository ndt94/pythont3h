from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def createProduct(code, name, price):
        Product.objects.create(code=code, name=name, price=price)