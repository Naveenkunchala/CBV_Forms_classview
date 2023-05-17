from django.db import models

# Create your models here.

class School(models.Model):
    SNAME=models.CharField(max_length=100)
    SID=models.IntegerField(primary_key=True)
    SADDRESS=models.TextField(max_length=200)
