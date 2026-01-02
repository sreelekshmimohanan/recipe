from django.db import models


class tbl_login(models.Model):
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    user_type=models.CharField(max_length=150)
    
class customer_reg(models.Model):
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    street=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)