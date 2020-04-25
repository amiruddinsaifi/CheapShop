from django.db import models

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name=models.CharField(max_length=30)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    pub_date = models.DateField()
    product_image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name

class Contect(models.Model):
    msg_id=models.AutoField(primary_key='msg_id')
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=100)


    def __str__(self):
        return self.name