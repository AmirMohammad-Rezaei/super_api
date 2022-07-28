from django.db import models


# Create your models here.

class Food_Db(models.Model):
    fname = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name="قیمت")
