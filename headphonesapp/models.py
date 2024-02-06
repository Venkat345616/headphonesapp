from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class products(models.Model):


    category = models.CharField(max_length=50)
    launch = models.CharField(max_length=50) 
    brand = models.CharField(max_length=50)
    brand_image =models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    image1 = models.ImageField(upload_to='uploads/products/')
    image2 = models.ImageField(upload_to='uploads/products/')
    image3 = models.ImageField(upload_to='uploads/products/')
    image4 = models.ImageField(upload_to='uploads/products/')
    image5 = models.ImageField(upload_to='uploads/products/')
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    accessories = models.BooleanField(default=False)
    wired_or_TWS = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField(default=0)
    offer = models.IntegerField(default=0)



    def __str__(self):
        return self.name



    class Meta:
        db_table = 'products'




class myUser(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    number = models.CharField(max_length = 225)
    
    

    def __str__(self):
        return self.user.username



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
