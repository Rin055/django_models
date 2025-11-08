from django.db import models

class Furniture(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    has_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.title
