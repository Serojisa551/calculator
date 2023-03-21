from django.db import models

class Testing(models.Model):
    name = models.CharField(max_length= 255)
    phone = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.name}"
