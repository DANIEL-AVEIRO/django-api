from django.db import models

# Create your models here.


class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
