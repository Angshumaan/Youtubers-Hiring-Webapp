from django.db import models

# Create your models here.


class Info(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    fb = models.CharField(max_length=254)
    insta = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)

    def __str__(self):
        return self.email
