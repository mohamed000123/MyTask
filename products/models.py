from django.db import models
from users.models import User


class Products (models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    
