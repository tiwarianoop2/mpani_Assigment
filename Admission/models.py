from django.db import models

# Create your models here.


class Students(models.Model):
    Name=models.CharField(max_length=100)
    Stream=models.CharField(max_length=100)
    Session=models.CharField(max_length=100)
    Class=models.IntegerField(default=0)
    Previous_Remark=models.CharField(max_length=100)
