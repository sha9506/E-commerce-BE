from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length= 300)
    product_price = models.IntegerField(max_length=10)
    icon = models.CharField(max_length=300)
    
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10, null=True, unique=True)
    
