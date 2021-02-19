from django.db import models

from django.utils import timezone

# Create your models here.
class Fruit(models.Model):
    fruit_type = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    path= models.CharField(max_length=250)