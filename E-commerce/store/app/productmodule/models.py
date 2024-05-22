from django.db import models

class customers(models.Model):
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    phone = models.BigIntegerField(default = 0000000000)
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    

class products(models.Model):
    id = models.BigAutoField(primary_key = True)
    p_name = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    p_count = models.IntegerField()
    price = models.IntegerField()
    p_image = models.ImageField(null=True, blank=True, upload_to="image/")
    
    
class carts(models.Model):
    id = models.BigAutoField(primary_key = True)
    p_id = models.IntegerField(default = 0)
    p_name = models.CharField(max_length = 20)
    p_count = models.IntegerField(default = None)
    price = models.IntegerField()
    p_img = models.ImageField(null=True, blank=True)
    