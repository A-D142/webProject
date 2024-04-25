from django.db import models

class customer(models.Model):
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length = 20)
    phone = models.BigIntegerField(default = 0000000000)
    username = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    

class add_product(models.Model):
    id = models.BigAutoField(primary_key = True)
    p_name = models.CharField(max_length = 20)
    company = models.CharField(max_length = 20)
    p_count = models.IntegerField()
    img_num = models.IntegerField()
    