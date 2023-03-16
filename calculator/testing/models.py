from django.db import models

class Testing(models.Model):
    name = models.CharField(max_length= 255)
    phone = models.ImageField(null = True)