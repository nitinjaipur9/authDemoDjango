from django.db import models

# Create your models here.
class customUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email