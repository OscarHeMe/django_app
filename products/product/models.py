from django.db import models


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
